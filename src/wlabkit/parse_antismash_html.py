import os
from collections import namedtuple
import pandas as pd
from bs4 import BeautifulSoup


class AntismashIndexHtmlParser():
    def __init__(self, index_html):
        self.index_html = index_html

    @property
    def soup(self):
        return BeautifulSoup(open(self.index_html), features="html.parser")

    def get_predicted_core_structure(self):
        """
        Parse index.html and extract predicted core structure(s) information.
        {(CP002995.1, Region 1, NRPS+betalactone): {location: smi}}
        """

        # seq_id_ls, region_num_ls, bgc_type_ls = [], [], []
        # location_start_ls, location_end_ls, smi_ls = [], [], []
        genome_structure_dict = {}

        region_pages = self.soup.select('div[class="page"]')
        for region_page in region_pages:
            # 获取每个region信息
            RegionInfo = namedtuple('RegionInfo', ['seq_id', 'region_num', 'bgc_type'])
            if region_page.attrs['id'] == 'overview':
                continue
            region_description = region_page.find(name='div', attrs={'class': 'heading'}).contents[0]
            region_info = RegionInfo(*region_description.strip().split(' - '))

            # 获取每个region里的结构信息（每个region可能有多个结构信息）
            region_structure_dict = {}
            structures = region_page.select('div[class="structure"]')
            for structure in structures:
                prediction_text = structure.find(name='div', attrs={'class': 'prediction-text'}).contents
                if prediction_text:
                    location = prediction_text[0].strip().rstrip(':').split('location ')[1].split(' - ')
                    location_start, location_end = location
                    smi = structure.select('canvas[class="smiles-canvas"]')[0]['data-smiles']
                    region_structure_dict[(location_start, location_end)] = smi
            if region_structure_dict:
                genome_structure_dict[region_info] = region_structure_dict
        return genome_structure_dict


def get_antismash_structures(args):
    html_ls = []
    if args.html_list:
        with open(args.html_list, 'r') as fl:
            html_ls = fl.read().splitlines()
            html_ls = list(set(html_ls))
    if args.input_html:
        html_ls.append(args.input_html)

    structures_df_ls = []
    for html in html_ls:
        antismash_index_html = AntismashIndexHtmlParser(html)
        structures_dict = antismash_index_html.get_predicted_core_structure()
        seq_id, region_num, bgc_type = [], [], []
        location_start, location_end, smi = [], [], []

        for seq_info, structures in structures_dict.items():
            for location, smiles in structures.items():
                seq_id.append(seq_info.seq_id)
                region_num.append(seq_info.region_num)
                bgc_type.append(seq_info.bgc_type)
                location_start.append(location[0])
                location_end.append(location[1])
                smi.append(smiles)
        structures_df = pd.DataFrame({
            'seq_id': seq_id,
            'region_num': region_num,
            'BGC_type': bgc_type,
            'location start': location_start,
            'location end': location_end,
            'SMILES': smi
        })
        structures_df_ls.append(structures_df)
    pd.concat(structures_df_ls).to_csv(args.output_file, sep='\t', index=False)
