#!/usr/bin/env python

from Bio import SeqIO


def get_target_seq(args):
    with open(args.target_list, 'r') as fl:
        target_seq_header = fl.read().splitlines()
        target_seq_header = list(set(target_seq_header))
        print(f'Target list: {len(target_seq_header)} sequence(s)')
    target_records = []
    for seq_record in SeqIO.parse(args.input_fasta, "fasta"):
        seq_desc = seq_record.description
        seq_id = seq_record.id
        if seq_desc in target_seq_header:
            target_records.append(seq_record)
            target_seq_header.remove(seq_desc)
        elif seq_id in target_seq_header:
            target_records.append(seq_record)
            target_seq_header.remove(seq_id)
    print(f'No match: {len(target_seq_header)} sequence(s) ')
    # print no match list
    if len(target_seq_header) > 0:
        print('No match list:')
        for h in target_seq_header:
            print(h)
    SeqIO.write(target_records, args.output_fasta, "fasta")
