no = int(input("Enter number of equations you have"))
aarr = []
narr = []
for i in range(no):
    print(f"Enter value of a{i+1} in x ≅ a{i+1}(mod n{i+1})")
    tempa = int(input())
    aarr.append(tempa)
    print(f"Enter value of n{i+1} in x ≅ a{i+1}(mod n{i+1})")
    tempn = int(input())
    narr.append(tempn)

n=1
for i in range(no):
    n*=(narr[i])

Narr = []
for i in range(no):
    Narr.append(n//(narr[i]))

def inverse(a, b, p):
    result = 1
    a = a % p

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % p

        a = (a * a) % p
        b = b // 2

    return result

Marr = []
for i in range(no):
    Marr.append(inverse(int(Narr[i]), (narr[i] - 2), narr[i]))


x=0
for i in range(no):
    x+=(aarr[i]*Narr[i]*Marr[i])

print(x%n)