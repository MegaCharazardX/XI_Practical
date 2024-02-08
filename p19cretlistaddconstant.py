fst = []
n = int(input("Enter number of elements :"))
for i in range (0,n):
    ele = int (input ("Enter the element : "))
    fst. append (ele)
addno = int(input("Enter the number to add : "))
fst2 = [x + addno for x in fst]
print ("The second list is : ",fst2)
input()
