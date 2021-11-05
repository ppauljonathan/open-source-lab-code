from random import seed,random

def num_bin(num):
    k=list(bin(int(num)).split('b')[1])
    while(len(k)%8!=0):
        k.insert(0,'0')
    return k
    

def num_with_range(n):
    return int(n*8+1)

def rev_shift(ar,n):
    arr=list(ar)
    for i in range(0,n):
        a=arr.pop()
        arr.insert(0,a)
    return arr

def xor_s(s1,s2):
    if s1==s2:
        return '0'
    else:
        return '1'

def div_8_pl(mcip):
    div_8=[]
    k=[]
    for i in range(0,len(mcip)):
        k.append(mcip[i])
        if i%8==7:
            div_8.append(k)
            k=[]
    return div_8

def make_plain(k):
    kar=list(k)
    return int("".join(kar),2)

def main():
    raw=input("enter ciphertext : ")
    parsed_raw=raw[1:len(raw)-1].split(', ')
    seed(int((len(parsed_raw)-1)/2))
    sup_round=int(parsed_raw[-1])
    parsed_raw.pop()
    gens=[]
    for i in range(0,sup_round+1):
        gens.append(num_with_range(random()))
    
    bin_cip_raw=[]
    for i in parsed_raw:
        bin_cip_raw.append(num_bin(i))

    cip=[]
    key=[]
    for i in bin_cip_raw[:int(len(bin_cip_raw)/2)]:
        for j in i:
            cip.append(j)
    for i in bin_cip_raw[int(len(bin_cip_raw)/2):]:
        for j in i:
            key.append(j)

    mcip=list(cip)
    gens.reverse()
    gens.pop()

    for i in gens:
        for j in range(0,len(key)):
            mcip[j]=xor_s(mcip[j],key[j])
        key=rev_shift(key,i)

    plain_8=div_8_pl(mcip)
    plain_ascii=[]
    for i in plain_8:
        plain_ascii.append(make_plain(i))
    
    plain_chr=[]

    for i in plain_ascii:
        plain_chr.append(chr(i))

    decrypted="".join(plain_chr)

    print(decrypted)
    return

main()