import os
from pprint import pprint

from Bio import SeqIO


def input_type(input):
    """Determine if the input is a file or folder.

    Args:
        input: Path of file or folder

    Returns:
        If input is a file, return "file".
        If input is a folder, return "folder".
    """

    if os.path.isdir(input):
        return "folder"
    elif os.path.isfile(input):
        return "file"
    else:
        raise Exception('Unable to recognize input')


def get_seq_records(gene_file, file_type):
    """Parse a gene file.

    Args:
        gene_file: A file containing genes in fasta or genbank format.
        file_type: String of "genbank" or "fasta"

    Returns:
        A list of seq record objs.
    """

    seq_records = []
    for seq_record in SeqIO.parse(gene_file, file_type):
        seq_records.append(seq_record)
    return seq_records


def gbk2fasta(gbk, merge=True):
    """Convert gbk file to fasta file.

    Args:
        gbk: A gbk file input.
        merge: If true, all gbk file will merge to a fasta file. Otherwise, a gbk file outputs a fasta file.

    Returns:
        A list of seq record objs.
    """

    in_type = input_type(gbk)
    if in_type == 'folder':
        file_names = os.listdir(gbk)
        file_dirs = [os.path.join(gbk, name) for name in file_names]
        merged_seq_records = []
        no_merged_seq_records = {}
        for file in file_dirs:
            one_file_seq_records = get_seq_records(file, 'genbank')
            if merge:
                merged_seq_records += one_file_seq_records
            else:
                fasta_file_name = os.path.splitext(os.path.basename(file))[0] + '.fna'
                no_merged_seq_records[fasta_file_name] = one_file_seq_records

        if merge:
            return merged_seq_records
        else:
            return no_merged_seq_records

    if in_type == 'file':
        seq_records = get_seq_records(gbk, 'genbank')
        return seq_records


def write_fasta(seq_records, output):
    """Save seq records to file(s).

    Args:
        seq_records: Seq record objs.
        output: A file path if output is a file. A folder path if output is multiple files.

    Returns:
        Saved files.
    """

    if isinstance(seq_records, list):
        SeqIO.write(seq_records, output, "fasta")
    if isinstance(seq_records, dict):
        for fn, seq in seq_records.items():
            SeqIO.write(seq, os.path.join(output, fn), "fasta")


def gbk2fasta_pipeline(args):
    seq = gbk2fasta(args.input, args.merge)
    write_fasta(seq, args.output)
