import os

from wlabkit.parse_gbk import get_seq_records, input_type, write_fasta


def get_sl_seq(fasta, l, r):
    """Get seq record objs with specified length.

    Args:
        fasta: A fasta file.
        l: Specifies the minimum length of a sequence. The left edge of the length range and includes the edge value.
        r: Specifies the maximum length of a sequence. The right edge of the length range and includes the edge value.

    Returns:
        A list of specified length seq record objs.
    """

    sl_seq_records = []
    seq_records = get_seq_records(fasta, 'fasta')
    for seq_record in seq_records:
        seqlen = len(seq_record.seq)
        if l <= seqlen <= r:
            sl_seq_records.append(seq_record)
    return sl_seq_records


def exsl_seq(fasta, l, r, merge=False):
    """Extract specified length of sequence.

    Args:
        fasta: A fasta file or a folder containing fasta files.
        merge: If true, all gbk file will merge to a fasta file. Otherwise, a gbk file outputs a fasta file.
        l: Specifies the minimum length of a sequence. The left edge of the length range and includes the edge value.
        r: Specifies the maximum length of a sequence. The right edge of the length range and includes the edge value.

    Returns:
        A list or a dict of specified seq record objs.
    """
    in_type = input_type(fasta)
    if in_type == 'folder':
        file_names = os.listdir(fasta)
        file_dirs = [os.path.join(fasta, name) for name in file_names]
        merged_seq_records = []
        no_merged_seq_records = {}
        for file in file_dirs:
            one_file_seq_records = get_sl_seq(file, l, r)
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
        seq_records = get_sl_seq(fasta, l, r)
        return seq_records


def exsl_seq_pipeline(args):
    sl_seq = exsl_seq(args.input, args.left, args.right, args.merge)
    write_fasta(sl_seq, args.output)
