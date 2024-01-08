CODONS_LIST = {"Methionine": ["AUG"], "Phenylalanine": ["UUU", "UUC"], "Leucine": ["UUA", "UUG"],
               "Serine": ["UCU", "UCC", "UCA", "UCG"], "Tyrosine": ["UAU", "UAC"], "Cysteine": ["UGU", "UGC"],
               "Tryptophan": ["UGG"], "STOP": ["UAA", "UAG", "UGA"]}
CODONS = {codon: protein for protein, codons in CODONS_LIST.items() for codon in codons}


def proteins(strand):
    proteins_list = []
    cod_list = [strand[i:i + 3] for i in range(0, len(strand), 3)]
    for cod in cod_list:
        if CODONS[cod] == "STOP":
            return proteins_list
        proteins_list.append(CODONS[cod])
    return proteins_list
