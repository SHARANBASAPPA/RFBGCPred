from Bio import SeqIO

def extract_sequence_from_fasta(fasta_file):
    """Extract sequences from a FASTA file."""
    sequences = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequences.append(str(record.seq))
    return sequences

def extract_sequence_from_gbk(gbk_file):
    """Extract sequences from a GenBank file."""
    sequences = []
    for record in SeqIO.parse(gbk_file, "genbank"):
        for feature in record.features:
            if feature.type == "CDS" and 'translation' in feature.qualifiers:
                sequences.append(feature.qualifiers['translation'][0])
    return sequences
