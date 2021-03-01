#!/usr/bin/env python
"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""
from CountingDNANucleotides import txt_to_str
complementing_dict = {
  "A" : "T",
  "C" : "G",
  "G" : "C", 
  "T" : "A",
}

def complementing(dna_seq):
    rna_seq=[complementing_dict[nucleotide] for nucleotide in dna_seq[-1::-1]]
    return ''.join(rna_seq) 

if __name__ == "__main__":
    s=txt_to_str("rosalind_revc.txt").rstrip("\n")
    sc=complementing(s)
    print(sc)
