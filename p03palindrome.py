print ("This is a program to find wether the entered word is palindrome or not. ")
string = input("Enter the string : ")
reverse = string[: : -1]
if reverse == string :
    print ("The entered string is palindrome")
else :
    print ("The entered string is not palindrome")
input()
    
