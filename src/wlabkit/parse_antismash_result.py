#!/usr/bin/env python

from Bio import SeqIO
import os
import webbrowser
import zipfile
import pandas as pd



class Antismash_gbk_parser():
    """parse antiSMASH gbk file and extract something needed"""
    def __init__(self):
        self.type = []

    def extract_BGC_type(self, gbk):
        for seq_record in SeqIO.parse(gbk, "genbank"):
            features = seq_record.features
            for feature in features:
                if feature.type == 'protocluster':
                    product = feature.qualifiers['product']
                    self.type += product
        return product


class Antismash_result_folder():
    """read an antiSMASH result folder and extract something needed"""
    def __init__(self, folder_path, decompression=False):
        """initialize features"""

        "get folder path"
        self.path = folder_path

        "get folder name"
        self.basename = os.path.basename(folder_path)

        "get folder dirname"
        self.dirname = os.path.dirname(folder_path)

        "get BGC region bgk files"
        self.region_gbk = []
        self.region_gbk_dir = []

        "get index.html in folder"
        self.index_html = ''
        self.index_html_dir = ''

        if zipfile.is_zipfile(self.path):
            if decompression:
                self.decompression()

                "get files in folder"
                self.path = os.path.join(self.dirname, self.basename)
                self.file = os.listdir(self.path)

            else:
                raise Exception("Input folder is a ZIP file, Please set argument 'decompression' as True.")

        else:
            "get files in folder"
            self.file = os.listdir(self.path)


        self.get_target_file()

    def decompression(self):
        """decompresse zip file to the current folder with name unchanged"""
        zip_file = zipfile.ZipFile(self.path)
        self.basename = self.basename.rstrip('.zip')
        zip_file.extractall(os.path.join(self.dirname, self.basename))
        zip_file.close()


    def get_target_file(self):
        for f in self.file:
            suffix = '.gbk'
            key_word = 'region'
            if (f.endswith(suffix)) and (key_word in f):
                self.region_gbk.append(f)
                self.region_gbk_dir.append(os.path.join(self.path, f))
            if f == 'index.html':
                self.index_html = f
                self.index_html_dir = os.path.join(self.path, f)

    def open_index_html(self):
        index_html_url = 'file://' + self.index_html_dir
        webbrowser.open(index_html_url)

def find_target_gbk_dir(gbkdir_type_dict, target):
    target_dict = {}
    for k, v in gbkdir_type_dict.items():
        for target_v in target:
            if v == target_v:
                target_dict[k] = v
    return target_dict


def get_target_type_gbk_dir(args):
    try:
        with open(args.target_type) as fl:
            target_type = fl.read().splitlines()
    except:
        target_type = [args.target_type]

    antismash_folder = Antismash_result_folder(args.input_path, decompression=True)
    region_gbk_dir = antismash_folder.region_gbk_dir
    antismash_gbk_parser = Antismash_gbk_parser()
    for dir in region_gbk_dir:
        antismash_gbk_parser.extract_BGC_type(dir)
    gbkdir_type_dict = dict(zip(region_gbk_dir, antismash_gbk_parser.type))
    target_dict = find_target_gbk_dir(gbkdir_type_dict, target_type)
    if args.output_file:
        target_df = pd.DataFrame({
            'gbk_dir': list(target_dict.keys()),
            'type': list(target_dict.values())
        })
        target_df.to_csv(args.output_file, index=False, header=None, sep='\t')
    else:
        for k, v in target_dict.items():
            print(f'{k}\t{v}')
