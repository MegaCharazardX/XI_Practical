num = int(input("Enter the number of elements : "))
fst = []
for i in range (num):
    ele = int (input ("Enter element no.:"))
    fst. append (ele)
fiel = int(input("Enter the element to find : "))
if(fiel in fst ) :
    print("Element found  ")
else :
    print("Element not found  ")
    

input()