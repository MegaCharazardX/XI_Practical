print("This is a program to find the largest of two value.")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
while True :
    numb1 = int(input("Please enter an value : "))
    numb2 = int(input("Please enter another value : "))
    if numb1 == numb2 :
        print("Both the values are same")
        continue
    elif numb1 > numb2 :
        print ("The greatest value is {0}".format(numb1))
    else  :
        print ("The greatest value is {0}".format(numb2))
        print ("Enter '1' to continue & anyother to quit")
        decision = int(input("Please enter what to do : ")) 
        if decision == 1:
            continue
            print("\n")            
        else :
            break
input()
        
        
        

