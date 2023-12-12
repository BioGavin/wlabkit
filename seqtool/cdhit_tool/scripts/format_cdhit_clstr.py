#! /usr/bin/env python3
# Author:ZhouZhenyi
# Description:format the cd-hit output file into excel
# Usage: python3 format_cdhit_clstr.py db90.fna.clstr
import argparse
import os.path
import re
import pandas as pd


def help():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
examples:
1. python format_cdhit_clstr.py -i nr80.fasta.clstr -o .
        '''
    )

    parser.add_argument('-i', '--input', required=True, type=str,
                        help='Input a single region GBK file or a list of antiSMASH result folder paths.')
    parser.add_argument('-o', '--output', required=True, type=str,
                        help='Specify the folder where the output files are stored.')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = help()

    seq_id = []
    cluster = []
    index = []
    length = []
    identity = []

    with open(args.input, "r") as f:  # 输入clstr文件
        line_ls = f.readlines()
    cluster_num = ""
    for line in line_ls:
        if line.startswith(">"):
            cluster_num = line.split(' ', 1)[1]
            continue
        cluster.append(cluster_num.strip('\n'))
        # 使用正则表达式提取">"和"at"之间的所有字符
        pattern = re.compile(r'>(.*?) ')
        # 查找匹配项
        match = pattern.search(line)
        # 如果匹配成功，获取匹配的内容
        if match:
            extracted_content = match.group(1)
            seq_id.append(extracted_content)
        else:
            print(f'Can not find seq header in {line}')

        index.append('Cluster' + cluster_num.strip() + '_' + line.split('\t', 1)[0])

        # 指定多个分割词，使用正则表达式的"或"运算符
        split_pattern = re.compile(r'aa|nt')
        # 使用re.split()进行分割
        length.append(split_pattern.split(line)[0].split('\t', 1)[1])

        if line.endswith("*\n"):
            identity.append('*')
            continue
        identity.append(line.split('at', 1)[1].strip())
    df = pd.DataFrame({'SeqID': seq_id,
                       'Cluster': cluster,
                       'Index': index,
                       'Length': length,
                       'Identity': identity})

    output_xlsx = os.path.join(args.output, os.path.basename(args.input).replace(".clstr", ".xlsx"))
    df.to_excel(output_xlsx, index=False)
