fst = []
n = int(input("Enter number of elements :"))
for i in range (0,n):
    ele = int (input ("Enter the element : "))
    fst. append (ele)
lesval = fst
lesval.sort()
minpos = fst.index(min(fst))
print("The least value is {0} and its index is {1}".format(lesval[0],minpos))
input()
