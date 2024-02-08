print("This is a program to find the largest of two value")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
while True :
    num = int(3)
    a = []
    for i in range (0,num):
        elem = int(input("Enter the element : "))
        a.append(elem)
        a.sort()
    maximum = a[-1]
    print ("The largest elements in the list is :",maximum)
    print ("Enter '1' to continue & anyother to quit")
    decision = int(input("Please enter what to do : "))
    if decision == 1:
        continue
    else :
        break
input()
    
        
