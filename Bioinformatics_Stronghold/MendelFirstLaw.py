#!/usr/bin/env python
def DominantPhenotype(k, m, n):
    pop=k+m+n
    aaxaa, AaxAa, Aaxaa= 0, 0, 0
    if n>1:
        aaxaa = (n/pop)*((n-1)/(pop-1))
    if m>1:
        AaxAa= (m/pop)*((m-1)/(pop-1))
    if (m>0) & (n>0):
        Aaxaa= (m/pop)*(n/(pop-1)) + (n/pop)*(m/(pop-1))
    prob= aaxaa + AaxAa*0.25 + Aaxaa*1/2
    return 1-prob

if __name__ == "__main__":
    k=int(input("k: "))  
    m=int(input("m: "))  
    n=int(input("n: "))  
    prob=DominantPhenotype(k, m, n)
    print(prob)
