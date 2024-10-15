def calculate_gc_content(dna):
    return (dna.count("G") + dna.count("C")) / len(dna) * 100

def get_reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    rev = dna[::-1]
    com = ''
    for i in rev:
        com += complement[i]
    return com


def translate_rna_to_protein(rna):
    return rna.replace('U', 'X')

def translate_dna_to_rna(dna):
    return dna.replace('T', 'U')

def translate_rna_to_dna(rna):
    return rna.replace('U', 'T')

if __name__ == "__main__":
    dna = 'TGCA' #ACGT   # TGCA
    print(calculate_gc_content(dna))
    print(get_reverse_complement(dna))
    

