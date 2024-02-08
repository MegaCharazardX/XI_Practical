num = int(input("Enter the number of elements : "))
a = []
for i in range (0,num):
    elem = int(input("Enter the element : "))
    a.append(elem)
avg = sum(a)/num
print ("The average of the elements in the list is :",avg)

input()