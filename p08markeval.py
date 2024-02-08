
"""while True :
    engmark=int(input("Enter the mark for English"))
    if engmark > 100 or engmark<0 :
        print(ErrMsg)
        continue
    else:
        break
while True :
    maxmark=int(input("Enter the mark for Mathematics"))
    if maxmark > 100 or maxmark<0 :
        print(ErrMsg)
        continue
    else:
        break
while True :
    physmark=int(input("Enter the mark for Physics"))
    if physmark > 100 or physmark<0 :
        print(ErrMsg)
        continue
    else:
        break
while True :
    chemmark=int(input("Enter the mark for Chemistry"))
    if chemmark > 100 or chemmark<0 :
        print(ErrMsg)
        continue
    else:
        break
while True :
    compmark=int(input("Enter the mark for Computer"))
    if compmark > 100 or compmark<0 :
        print(ErrMsg)
        continue
    else:
        break
total = compmark + chemmark + physmark + maxmark +engmark
print("The total mark is {0}.".format (total))"""
"""total = 0
while True :
    mark=int(input("Enter the mark for English"))
    if mark > 100 or mark<0 :
        print(ErrMsg)
        continue
    else:
        total = total+ mark
        break
while True :
    mark=int(input("Enter the mark for Mathematics"))
    if mark > 200 or mark<0 :
        print(ErrMsg)
        continue
    else:
        total = total+ mark
        break
while True :
    mark=int(input("Enter the mark for Physics"))
    if mark > 100 or mark<0 :
        print(ErrMsg)
        continue
    else:
        total = total+ mark
        break
while True :
    mark=int(input("Enter the mark for Chemistry"))
    if mark > 100 or mark<0 :
        print(ErrMsg)
        continue
    else:
        total = total+ mark
        break

print("The total mark is {0}.".format (total))"""


def EvaluateMark (_subject):
    while True :
        mark=int(input("Enter the mark for {0}".format (_subject)))
        if mark > 100 or mark<0 :
            print(ErrMsg)
            continue
        else:
            return mark


ErrMsg = "!!!Invalid mark !!! --> Enter mark \
between 0 and 100"
           
subjectlist = ['English','Mathamatics','Physics',
               'Chemistry','Computer'] 
total = 0
for subject in subjectlist:
    retmark = EvaluateMark(subject)
    #print("The {0} mark is {1}.".format (subject , retmark))
    total = total + retmark
    persentage = float (total / 5)
    
print("The total mark is {0} and your persentage is {1}.".format(total , persentage))
if persentage >=80 :
    print("Your grade is A")

elif persentage >=60 and persentage <80 :
    print("Your grade is B")

elif persentage >=40 and persentage <60 :
    print("Your grade is C")

elif persentage >=20 and persentage <40 :
    print("Your grade is D")

else :
    print("Your grade is E")
input()











