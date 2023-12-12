import os.path

import pandas as pd


def get_fasta_list(list_file):
    with open(list_file, 'r') as f:
        fasta_list = f.read().splitlines()
    fasta_list = [line.strip() for line in fasta_list if line]
    fasta_list = list(set(fasta_list))
    return fasta_list


def get_header(fasta_file):
    header_list = []
    with open(fasta_file, "r") as f:
        content = f.readlines()
    for line in content:
        if line.startswith(">"):
            print(line)
            header = line[1:].strip()
            header_list.append(header)
    return header_list


def get_seq_header(args):
    df_ls = []
    fasta_list = get_fasta_list(args.fasta_list)
    for fasta in fasta_list:
        fasta_name = os.path.basename(fasta)
        header_list = get_header(fasta)
        data = {fasta_name: header_list}
        sub_df = pd.DataFrame(data).stack().reset_index(level=0, drop=True)
        sub_df.name = "header"
        sub_df.index.name = "file_name"
        df_ls.append(sub_df)
    df = pd.concat(df_ls)
    df.to_csv(args.output_tsv, sep="\t")
