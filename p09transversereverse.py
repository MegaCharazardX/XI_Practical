print ("This is a program to transverse and reverse a string")
string = input("Enter the string : ")
for i in string :
    print (i,end = '')
    print("\n")
reverse = string[: : -1]
print (f"This is the reversed form of {string} : {reverse}")
input()

