print("This is a program to calculate the formula E = mc².")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

m = float(input("Enter the mass of the object : "))
c = 3*10**8
e = m*c**2
print(f"The energy produced is {e} Joules")#"{:e}".format(e)
input()