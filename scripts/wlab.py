#!/usr/bin/env python

import sys
import os
sys.path.append('/Users/zhouzhenyi/Desktop/wlab/wlab')
print(sys.path)
import argparse
from wlab import getseq



# create the top-level parser
parser = argparse.ArgumentParser(
    prog='wlab.py',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
This is a toolkit to handle bio-data from WeiBin Lab.

Author: Gavin <gavinchou64@gmail.com>
Source code: https://github.com/BioGavin/wlab''',
    epilog='''
Use "wlab.py [subcommand] --help" for more information about a command''')

# create the sub-level parser
subparsers = parser.add_subparsers(title='subcommands')

# create the sub-parser for the "getseq" command
parser_getseq = subparsers.add_parser('getseq', help='get target sequences from a header list',
                                      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser_getseq.add_argument('-i', '--input_fasta', required=True,
                           type=str, help='fasta file for searching target sequences.')
parser_getseq.add_argument('-l', '--target_list', required=True,
                           type=str, help='a list file containing target sequence headers.')
# parser_getseq.add_argument('-L', '--local_matching', action='store_true', default=False,
#                            help='add this arguments, if target list only locally matches the fasta file header.')
parser_getseq.add_argument('-o', '--output_fasta', default='target.fasta',
                           type=str, help='output fasta file containing target sequences.')
parser_getseq.set_defaults(func=getseq.get_target_seq)


# create the sub-parser for the "test" command
# parser_test = subparsers.add_parser('test', help='test',
#                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# parser_test.add_argument('-i', required=True,
#                          type=str, help='input test')
# parser_getseq.set_defaults(func=getseq.test)


def main():
    args = parser.parse_args()
    getseq.get_target_seq(input=args.input_fasta,
                          list=args.target_list,
                          output=args.output_fasta,
                          local_matching=args.local_matching)
    # getseq.test(i=args.i)


    # args_getseq = parser_getseq.parse_args()
    # getseq.get_target_seq(input=args_getseq.input_fasta,
    #                       list=args_getseq.target_list,
    #                       output=args_getseq.output_fasta,
    #                       local_matching=args_getseq.local_matching)

if __name__ == '__main__':
    main()




