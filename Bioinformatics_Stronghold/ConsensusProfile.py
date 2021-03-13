#!/usr/bin/env python
import pandas as pd
from Bio import SeqIO
import numpy as np
"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""

def FastaToDNA_String(input_file):
    with open(input_file) as fasta_file:
        seq = [seq_record.seq for seq_record in SeqIO.parse(fasta_file, 'fasta')]
    s = pd.Series(seq, name='sequence')
    df = pd.DataFrame(dict(sequence=s))
    return df
def DNA_StringToProfile(df):
    n=len(df['sequence'][0])
    profile = { 'T':[0]*n,'G':[0]*n ,'C':[0]*n,'A':[0]*n }
    for index, row in df.iterrows():
        for i, nucleotide in enumerate(row['sequence']):
            profile[nucleotide][i] += 1
    dfm = pd.DataFrame(dict(A=profile['A'], C=profile['C'],G=profile['G'], T=profile['T']))
    return dfm

def ConsensusString(dfm):
    maxValueIndexObj = dfm.idxmax(axis=1)
    print(''.join(maxValueIndexObj))
    return ''.join(maxValueIndexObj)

def main(input_file):
    df=FastaToDNA_String(input_file)
    dfm=DNA_StringToProfile(df)
    string=ConsensusString(dfm)
    with open('ConsensusProfile.txt', 'w') as f:
        f.write(string)
        f.write('\n')
        f.write('A: {0}\n'.format(' '.join(f'{y}' for y in dfm.T.values[0])))
        f.write('C: {0}\n'.format(' '.join(f'{y}' for y in dfm.T.values[1])))
        f.write('G: {0}\n'.format(' '.join(f'{y}' for y in dfm.T.values[2])))
        f.write('T: {0}\n'.format(' '.join(f'{y}' for y in dfm.T.values[0])))
if __name__ == "__main__":
    main('rosalind_cons.txt')

    main('example.txt')

