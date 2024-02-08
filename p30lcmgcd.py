x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

if x > y :
    smaller = y
else : 
    smaller = x
for i in range(1, smaller + 1):
    if((x % i == 0) and (y % i == 0)) :
        hcf = i
lcm = (x*y) / hcf
print(f"The GCD of {x} and {y} is : {hcf}")
print(f"The LCM of {x} and {y} is : {lcm}")
input()