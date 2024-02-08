print("This is a program to sum the '1 + x + x^2 + ... + x^n")
xvalue = float(input("Please enter the value of 'x' : "))
nvalue = int(input("Please enter the value of 'n' : "))
sumxv = 0
for i in range (nvalue + 1) :
    sumxv +=  xvalue ** i
print ("The sum of the series is :",int(sumxv))
input()
