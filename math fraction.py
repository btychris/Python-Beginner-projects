#Maths Fraction Hack Algorithm - www.101computing.net/maths-fraction-hack-algorithm/

a = int(input("Enter the numerator of the first fraction:"))
b = int(input("Enter the denominator of the first fraction:"))
print("First Fraction: " + str(a) + "/" + str(b))

# 1 - Complete the code here to enter the second fraction
c = int(input("Enter the numerator of the first fraction:"))
d = int(input("Enter the denominator of the first fraction:"))
print("Second Fraction: " + str(c) + "/" + str(d))
# 2 - Complete the code here to calculate and compare the cross-products. Output which fraction is bigger
First = a * d
Second = b * c
if First > Second:
    print(f"{a}/{b} > {c}/{d}")
elif First < Second:
    print(f"{a}/{b} < {c}/{d}")
elif First == Second:
    print(f"{a}/{b} = {c}/{d}")

# 3 - Complete the code here to output the decimal value of both fractions

print(f"{a} x {d} = {First}")
print(f"{b} x {c} = {Second}")