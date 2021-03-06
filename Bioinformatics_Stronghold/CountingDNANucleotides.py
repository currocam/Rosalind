#!/usr/bin/env python
"""
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

from collections import Counter
def CountingDNANucleotides(str_seq):
    cc=Counter(str_seq)
    print("{0} {1} {2} {3}".format(cc['A'], cc['C'], cc['G'], cc['T']))

def txt_to_str(file='rosalind_dna.txt'):
    with open(file,"r") as f:
        str_seq = f.read()
    return str_seq

if __name__ == "__main__":
    str_seq=txt_to_str()
    CountingDNANucleotides(str_seq)
