#!/usr/bin/env python
from RNACodonTable import RNACodonDict

def translating(RNA_string):
    CodonString=[RNA_string[i:i+3] for i in range(0, len(RNA_string), 3)]
    ProteinString=[]
    for i in range(0, len(RNA_string), 3):
        codon=RNA_string[i:i+3]
        aa=RNACodonDict[codon]
        if aa=='Stop':
            break
        else:
            ProteinString.append(aa)
    return ProteinString
if __name__ == "__main__":
    with open('rosalind_prot.txt') as f:
        RNA_string = f.read().replace('\n', '')
    protein=translating(RNA_string)
    print("".join(protein))
