print("This is a program to calculate simple intrest.")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
#PNR/100
p = float(input("Please enter the principle amount : "))
n = float(input("Please enter the time period in years : "))
r = float(input("Please enter the rate of intrest : "))
si = (p*n*r)/100
print(f"The Simple Intrest for principle {p}, time {n}, at rate {r} is {si}")
print(f"The total payable amount : {p + si}")


input()