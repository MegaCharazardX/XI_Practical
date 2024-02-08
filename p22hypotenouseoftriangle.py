print("This is a program to calculate the hypotenues of a triangle.")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
s1 = float(input("Please enter the length of side 1 : "))
s2 = float(input("Please enter the length of side 2 : "))
py_s1 = s1**2
py_s2 = s2**2
py_s3 = py_s2 + py_s1

if py_s1 + py_s2 != py_s3 :
    print("!!!These side do not form a right angle triangle!!!")
else: 
    print(f"The hypotenouse is {py_s3**1/2}.")
input()