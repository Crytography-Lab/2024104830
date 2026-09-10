def phi(n):
    result = n;
    p=2;
    while p*p<=n:
        if n%p==0:
            while n%p==0:
                n = n//p
            result = result - result//p
        p = p+1
    if n>1:
        result = result - result//n
    return int(result)

a = int(input("Enter value of a "))
n = int(input("Enter value of n "))
if a>n:
    c = a
    d = n
else:
    c = n
    d = a

while(d!=0):
    temp = c % d
    c = d
    d = temp

if(c==1):
    print("Eligible as gcd(a,n) is 1")
    cal = a**phi(n)
    print(f"{cal} ≅ 1(mod{n})")
else:
    print("Not eligible as gcd(a,n) is not 1")