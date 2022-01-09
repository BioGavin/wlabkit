#!/usr/bin/env python

from Bio import SeqIO


def get_target_seq(args):
    with open(args.target_list, 'r') as fl:
        target_seq_header = fl.read().splitlines()
    target_records = []
    for seq_record in SeqIO.parse(args.input_fasta, "fasta"):
        seq_desc = seq_record.description
        if seq_desc in target_seq_header:
            target_records.append(seq_record)
        seq_id = seq_record.id
        if seq_id in target_seq_header:
            target_records.append(seq_record)
    SeqIO.write(target_records, args.output_fasta, "fasta")
