from random import seed,random

def make_bin(l):
    lbin=[]
    for i in l:
        lbin.append(list(bin(ord(i)).split('b')[1]))

    for i in lbin:
        while(len(i)<8):
            i.insert(0,'0')

    end=[]
    for i in lbin:
        for j in i:
            end.append(j)
    return end

def xor_s(s1,s2):
    if s1==s2:
        return '0'
    else:
        return '1'

def shift(ar,n):
    arr=list(ar)
    for i in range(0,n):
        a=arr.pop(0)
        arr.append(a)
    return arr

def num_with_range(n):
    return int(n*8+1)

def bin_to_dec(cip_8):
    k=[]
    cip_10=[]
    for i in range(0,len(cip_8)):
        k.append(cip_8[i])
        if(i%8==7):
            cip_10.append(int("".join(k),2))
            k=[]
    return cip_10

def main():
    plain=input("enter plaintext : ")
    seed(len(plain))
    plain_8_bit=make_bin(plain)
    mplain=list(plain_8_bit)
    rounds=num_with_range(random())
    splain=list(plain_8_bit)
    for j in range(0,rounds+1):
        splain=shift(splain,num_with_range(random()))
        for i in range(0,len(splain)):
            mplain[i]=xor_s(mplain[i],splain[i])

    cipher_8_bit=list(mplain)
    cipher_8_bit+=splain
    cipher_dec=bin_to_dec(cipher_8_bit)
    cipher_dec.append(rounds+1)
    print(cipher_dec)
    

main()

    


