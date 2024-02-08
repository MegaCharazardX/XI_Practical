import time
import sys
import random 
from time import sleep
from colorama import init, Fore
import Loading as LD

#animation = "😡😀🤢🥶"  #"😊🤣😍😒""""|/-\\"
start_time = time.time()


def tprint(words):
    for char in words:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()


print ("This is a program to roll a dice")
fun = input("Hit enter to start the program.")
if fun == "":
    while True :
        # while True:
        #     for i in range(100):
        #         time.sleep(0.05)  # Feel free to experiment with the speed here
        #         sys.stdout.write("\rYour dice is rolling " + animation[i % len(animation)])
        #         sys.stdout.flush()
        #     if time.time() - start_time > 5:  # The animation will last for 10 seconds
        #         break
        # sys.stdout.write("\rDone!")
        # print ("")
        LD.loading(animation= "!/-\\", text = "Your dice is rolling ")
        rolledvalue = random.randint(1,6)
        #print(Fore.BLUE)
        print ("\nYour number is : ", end = "")
        tprint(f"{rolledvalue}" ) #{Fore.BLUE}
        #print(Fore.WHITE)
        print ("\nDo you want to roll again ? \nEnter '1' to roll again and any other to quit .")
        dicision = input ("Enter your dicision :  ")
        if dicision == '1' :
            continue
        else :
            print ("Thank You !")
            break
        
else :
    print ("Thank You !")



input()