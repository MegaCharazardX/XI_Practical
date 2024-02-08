print("Program to find armstrong number")
numbertofind = int(input("Enter a number to check if it is amstrong number : "))
numblist = list(str(numbertofind))
finalval = 0
for i in range (0,len(numblist)) :
    current_value = int(numblist[i])
    #armstrong = current_value**len(numb)
    temp = 1
    for j in range (0,len(numblist)):
        temp = temp*current_value

    finalval = finalval +  temp

print(f"The sum of the power {len(numblist)} of {numbertofind} is {finalval}. Hence\
it is {'an Amstrong Number'if (numbertofind == finalval) else 'not an Amstrong Number'}")



#print("The sum of the power {0} of {1} is {2}. Hence it is {3}."
#.format(len(numblist),numbertofind,finalval,
#'an Amstrong Number' if (numbertofind == finalval)
#else 'not an Amstrong Number'))


#print("The sum of the power of {0}  is {1}.".format(numbertofind,finalval))
"""if finalval == numbertofind :
    print("The given number is an Armstrong number ")
else :
    print("The given number is not an Armstrong number ")"""
input()
