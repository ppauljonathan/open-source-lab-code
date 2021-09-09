def gcd(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a

def main():
    a=int(input("no1 : "))
    b=int(input("no2 : "))
    print(gcd(a,b))

main()
