n = int(input("Enter how many terms : "))
term = n +2
first = 0
second = 1
print("The fibonacci series : ")
print( f"{first} , {second}", end = ", ")

for i in range(2, term):
    next = first + second
    if i == term -1 :
        print(next, end = " ")
    else:
        print(next, end = ", ")
    
    first, second = second, next

input()
