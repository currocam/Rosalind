#!/usr/bin/env python

from Bio import SeqIO
def GC_Content(sequence):
    content=sequence.count('G') + sequence.count('C')
    per=content/len(sequence)*100
    return per

def ComputingFromFASTA(input_file):
    fasta_sequences = SeqIO.parse(open(input_file),'fasta')
    FASTA_ID=[]
    max_GC=-1
    for fasta in fasta_sequences:
        name, GC  = fasta.id, GC_Content(str(fasta.seq))
        if GC>max_GC:
            FASTA_ID=name
            max_GC=GC
    return FASTA_ID, max_GC

if __name__ == "__main__":
    ID, maxGC= ComputingFromFASTA("rosalind_gc.txt")
    print(ID)
    print(maxGC)
