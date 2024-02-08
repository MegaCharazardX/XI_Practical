fst = []
n = int(input("Enter number of elements :"))
for i in range (0,n):
    ele = int (input ("Enter the element : "))
    fst. append (ele)
lis = fst
print ("The original list is :",lis)
lis = lis * 2
print ("The replicated list : ",lis)
fst.sort()
print ("The list in ascending order : ",fst)
fst.sort(reverse = True)
print ("The list in decending order : ",fst)

input()