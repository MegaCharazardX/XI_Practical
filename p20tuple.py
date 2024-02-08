tupinp =input("Enter the element with a space to seperate : ")
mytup = tuple(int(item) for item in tupinp.split())
print (mytup)
isFound = False
elem = int(input("Enter the element to find : "))
for i in mytup :
    if i == elem:
        isFound = True
        break
if(isFound):
   print("The element is found")
else :
    print("The element is not found")
    
input()
    

