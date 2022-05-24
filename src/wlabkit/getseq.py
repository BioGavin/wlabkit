#!/usr/bin/env python
from collections import namedtuple

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


def fasta2dictlist(fasta_file):
    """Parsing fasta file in a custom way.

    Args:
        fasta_file: The path of input fasta file.

    Returns: A list containing dictionaries.

    """
    with open(fasta_file, 'r') as f:
        lines = f.readlines()
    seq_records = []
    for line in lines:
        if line.startswith('>'):
            try:
                if seq_record:
                    seq_records.append(seq_record)
            except:
                pass
            seq_record = {}
            seq_record['header'] = line.replace('>', '').strip()
            seq_record['seq'] = ""
        else:
            seq_record['seq'] += line.strip()
    return seq_records


def get_target_seq2(args):
    """
    Get the target sequences by keyword in header.
    The keyword can be a part of the header.
    """
    with open(args.keyword_list, 'r') as fl:
        keyword_ls = fl.read().splitlines()
        keyword_ls = list(set(keyword_ls))
        print(f'keyword list: {len(keyword_ls)} keyword(s)')
    target_records = []

    for seq_record in SeqIO.parse(args.input_fasta, "fasta"):
        for keyword in keyword_ls:
            if (keyword in seq_record.name) or (keyword in seq_record.id) or (keyword in seq_record.description):
                target_records.append(seq_record)
                break
    print(f'get {len(target_records)} sequences in total.')
    SeqIO.write(target_records, args.output_fasta, "fasta")
