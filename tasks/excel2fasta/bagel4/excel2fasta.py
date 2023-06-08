import sys
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


def excel2fasta(excel, fasta):
    """

    Args:
        excel: Excel as an input holds the sequence information.
        fasta: Fasta as an output.

    Returns:
        A fasta file will be written.
    """

    target_col = ['NAME', 'ORGANISM', 'Sequence']
    seq_records = []

    data = pd.read_excel(excel, dtype=str)[target_col]
    for index, row in data.iterrows():
        name = str(row[target_col[0]]).strip()
        organism = str(row[target_col[1]]).strip()
        sequence = str(row[target_col[2]]).strip()
        seq_records.append(SeqRecord(Seq(sequence), id=name, description=organism))
    SeqIO.write(seq_records, fasta, 'fasta')


if __name__ == '__main__':
    excel_dir = sys.argv[1]
    fasta_dir = sys.argv[2]
    # excel_dir = 'bagel4_class1_demo.xlsx'
    # fasta_dir = 'bagel4_class1_demo.fasta'
    excel2fasta(excel_dir, fasta_dir)
