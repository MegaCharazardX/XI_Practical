noofstd = int(input("Enter the number of students : "))
result = {}
for i in range (noofstd):
    print("Enter details of students no.", i + 1)
    rollno = int(input ("Enter the Roll no :"))
    stdname = input("Student Name :")
    marks = int(input("Mark : "))
    result[rollno] = [stdname , marks]
    print(result)
input()