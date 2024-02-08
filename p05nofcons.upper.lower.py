print("This is a program to count the numbers of cosnsonents , upper & lower case charachters in a string")
string = str(input("Enter a string : "))
consonents = 0

lowercount = 0
for i in string :
    curentlower = string.islower()
    lowercount = lowercount + curentlower
print ("The number of lowercase characters is {0}".format(lowercount))
string1 = string
uppercount = 0
for i in string1 :
    curentupper = string1.isupper()
    uppercount = uppercount + curentupper
print ("The number of uppercase characters is {0}".format(uppercount)) 
input()
