#!/usr/bin/env python

def HammingDistance(seq1,seq2):
    if len(seq1)==len(seq2):
        dist=sum(nucleotide1 != nucleotide2 for nucleotide1, nucleotide2 in zip(seq1, seq2)) #wikipedia
        return dist

if __name__ == "__main__":
    with open('rosalind_hamm.txt') as f:
        seq1= f.readline()
        seq2=f.readline()
    dist=HammingDistance(seq1, seq2)
    print(dist)
