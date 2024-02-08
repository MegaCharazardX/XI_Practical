fst = []
n = int(input("Enter number of elements :"))
for i in range (0,n):
    ele = int (input ("Enter element no.:"))
    fst. append (ele)
fst.sort()
greatest = fst[-1]
print ("The greatest element is : ", greatest)
print(fst.index(greatest))
#for i in range (0, n):
#    for j in fst:
#        if j == greatest :
#            print ("The index of {0} is {1} ".format(greatest, i))
#        else:5

#
#            print("")
        

input()