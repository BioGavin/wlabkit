# ！/usr/bin/env python3

import argparse
from Bio import SeqIO


def help():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
examples:
1. check_seqname_unique -i seq.faa -k name
2. check_seqname_unique -i seq.faa -k id
        '''
    )

    parser.add_argument('-i', '--input', required=True, type=str,
                        help='Input FASTA file.')
    parser.add_argument('-k', '--key', required=True, type=str,
                        choices=["name", "id"], help='Sequence name or id.')

    args = parser.parse_args()
    return args


def get_seq(key, fasta_file):
    val_ls = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        if key == 'id':
            val_ls.append(record.id)
        if key == 'name':
            val_ls.append(record.name)
    return val_ls


if __name__ == '__main__':
    args = help()

    val_ls = get_seq(args.key, args.input)

    if len(val_ls) == len(set(val_ls)):
        print(f'sequence {args.key}s are unique.')
    else:
        print(f'sequence {args.key}s are not unique！')
