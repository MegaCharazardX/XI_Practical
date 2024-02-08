import random 
import Loading as LD
import sys
isrunning = True

while isrunning :
# Global Variabes
    Run = False
    running = True
    Comp_OddEven = ""
    Comp_baseorball = ""
    Toss_Winner = ""
    Toss_Comp = 0
    Toss_User = 0
    Toss_result = 0
    Comp_Choice = ""
    User_Choice = ""
    # print(sys.getsizeof(Toss_result))
    User_Bating_Result = 0
    Comp_Bating_Result = 0
    # User_Bowling_Result = 0
    # Comp_Bowling_Result = 0

    # ++++++++++FUNCTIONS++++++++++

    # Bating Or Bowling
    def _oddEven(_Comp_OddEven, _User_Toss):
        Comp_Toss = random.randint(0,6)
        Toss_result = _User_Toss + Comp_Toss
        if Toss_result % 2 == 0:
            if _Comp_OddEven == "E":
                #Toss_Winner = "Comp"
                return ["Comp", Toss_result]
            else:
                #Toss_Winner = "User"
                return ["User", Toss_result]
        else :
            if _Comp_OddEven == "O":
                #Toss_Winner = "Comp"
                return ["Comp", Toss_result]
            else:
                #Toss_Winner = "User"
                return ["User", Toss_result]
        
    # User Bating
    def _userBating(_UserBating):
        CompBowling = random.randint(0,6)
        if CompBowling + 1 == _UserBating or CompBowling - 1 == _UserBating:
            return "Out"
        elif CompBowling == _UserBating :
            return "2x"
        else : 
            return CompBowling 

    # Comp Bating
    def _compBating(_UserBowling):
        CompBating = random.randint(0,6)
        if CompBating + 1 == _UserBowling or CompBating - 1 == _UserBowling:
            return "Out"
        elif CompBating == _UserBowling :
            return "2x"
        else : 
            return CompBating 

    # Toss
    while True :
        
        User_OddEven = input("Odd or Even (O/E) : ")
        LD.loading(text = "")
        if User_OddEven == "O" or User_OddEven == "o":
            Comp_OddEven = "E"
            shouldContinue = True
            while shouldContinue :
                User_Toss = int(input("\nEnter toss number : "))
                LD.loading(text = "\r")
                if User_Toss > 6 or User_Toss < 0 :
                    print("\n!! Please Enter A Number Between 0 & 6 !!")
                    
                else:
                    Toss_Winner = _oddEven("E", User_Toss)
                    shouldContinue = False   
            break

        elif User_OddEven == "E" or User_OddEven == "e":
            Comp_OddEven = "O"
            shouldContinue = True
            while shouldContinue :
                User_Toss = int(input("\nEnter a number between 0 & 6 : "))
                LD.loading(text = "")
                if User_Toss > 6 or User_Toss < 0 :
                    print("\n!! Please Enter A Number Between 0 & 6 !!")
                    
                else:
                    Toss_Winner = _oddEven("O", User_Toss)
                    shouldContinue = False  
            break

        else :
            print("!!<-- Please Enter 'O' For Odd & 'E' For Even -->!!")
            continue

    print(f"\nComputer : {Toss_Winner[1] - User_Toss}")
    print(f"User : {User_Toss}")

    if Toss_Winner[0] == "Comp":
        print(f"Toss Winner: Computer")
    else:
        print(f"Toss Winner: User")

    if Toss_Winner[0] == "Comp" :
        LD.loading(text = "")
        Comp_Choice = random.choice(["Bating", "Bowling"])
        print("\nI Choose ", Comp_Choice, ".\n------Let's start the game.------\n")
    else :
        User_Choice = input("\nChoose bating or bowling (0/1) : ")
        LD.loading(text = "\r")
        if User_Choice  == "0" :
            User_Choice = "Bating"
            Comp_Choice = "Bowling"
            print("\nYou Chose ", User_Choice, ".\n")
        elif User_Choice == "1" :
            User_Choice = "Bowling"
            Comp_Choice = "Bating"
            print("\nYou Chose ", User_Choice, ".\n")

    for i in range(1):
        while User_Choice == "Bating" or Comp_Choice == "Bowling":
            if Run == True:
                break 
            User_Bating = int(input("\nYou're Batting : "))
            LD.loading(text = "")
            if User_Bating > 6 or User_Bating < 0 :
                print("\n!! Please Enter A Number Between 0 & 6 !!")
                continue
            else:
                User_Bating_function_val = _userBating(User_Bating)
                if User_Bating_function_val == "Out" and User_Bating_Result == 0 :
                    print("\nYou've Got A Duck Out !!")
                    print(f"Computer Entered : {User_Bating-1} \nYou Entered : {User_Bating} \nTotal : {User_Bating_Result} \n" )
                    User_Choice, Comp_Choice = "Bowling", "Bating"
                    Run = True
                    break
                if User_Bating_function_val == "Out":
                    print("\nYour Out !!\n")
                    if User_Bating == 0 :
                        print(f"Computer Entered : {User_Bating+1} \nYou Entered :  {User_Bating} \nTotal : {User_Bating_Result} " )
                    else :
                        print(f"Computer Entered : {User_Bating-1} \nYou Entered :  {User_Bating} \nTotal : {User_Bating_Result} " )
                        print("Your runs : ", User_Bating_Result, "\n")
                    User_Choice, Comp_Choice = "Bowling", "Bating"
                    Run = True
                    break
                # if User_Bating_Result > Comp_Bating_Result and i == 1:
                #     print("\nYou've Won!!")
                #     break
                elif User_Bating_function_val == "2x":
                    User_Bating_Result += User_Bating*2
                    print(f"\nYou Entered :  {User_Bating} \nComputer Entered : {User_Bating} \nTotal : {User_Bating_Result} \n" )
                    continue
                else :
                    if  User_Bating == 0 :
                        User_Bating_Result += User_Bating_function_val
                        print(f"\nComputer Entered : {User_Bating_function_val} \nYou Entered :  {User_Bating} \nTotal : {User_Bating_Result} \n" )
                        if Run and User_Bating_Result > Comp_Bating_Result :
                            print("I Won!!")
                            break
                        continue
                    else :    
                        User_Bating_Result += User_Bating
                        print(f"\nComputer Entered : {User_Bating_function_val} \nYou Entered :  {User_Bating} \nTotal : {User_Bating_Result} \n" )
                        if Run and User_Bating_Result > Comp_Bating_Result :
                            print("You Won")
                            break
                        continue

        while User_Choice == "Bowling" or Comp_Choice == "Bating":
            Userbowling = int(input("You're Bowling : "))
            LD.loading(text = "\r")
            if Userbowling > 6 or Userbowling < 0 :
                print("\n!! Please Enter A Number Between 0 & 6 !!")
                continue
            else:
                Comp_Bating_function_val = _compBating(Userbowling)
                if Comp_Bating_function_val == "Out" and Comp_Bating_Result == 0 :
                    print("\nI've Got A Duck Out !!")
                    print(f"You Entered : {Userbowling} \nComputer Entered : {Userbowling -1} \nTotal : {Comp_Bating_Result} \n" )
                    User_Choice, Comp_Choice = "Bating", "Bowling"
                    Run = True
                    break
                if Comp_Bating_function_val == "Out":
                    
                    print("\nI'm Out !!\n")
                    if Userbowling == 0 :
                        print(f"Computer Entered : {Userbowling+1} \nYou Entered :  {Userbowling} \nTotal : {Comp_Bating_Result} " )
                    else :
                    #print("\n", "-+"*10, "I'm Out !!","-+"*10)
                        print(f"You Entered :  {Userbowling} \nComputer Entered :  {Userbowling-1} \nTotal : {Comp_Bating_Result} " )
                        print("My runs : ", Comp_Bating_Result, "\n")
                    User_Choice, Comp_Choice = "Bating", "Bowling"
                    Run = True
                    break
                
                # if Comp_Bating_Result > User_Bating_Result and i == 1 :
                #     print("I've Won!!")
                #     break
                
                elif Comp_Bating_function_val == "2x":
                    Comp_Bating_Result += Userbowling*2
                    print(f"\nYou Entered : {Userbowling} \nComputer Entered : {Userbowling} \nTotal : {Comp_Bating_Result} \n" )
                    continue
                else :
                        
                    if  Comp_Bating_function_val == 0 :
                        Comp_Bating_Result += Userbowling
                        print(f"\nYou Entered : {Userbowling} \nComputer Entered : {Comp_Bating_function_val} \nTotal : {Comp_Bating_Result} \n" )
                        
                        if Run and Comp_Bating_Result > User_Bating_Result :
                            print("I Won")
                            break
                        continue
                    else : 
                        Comp_Bating_Result += Comp_Bating_function_val
                        print(f"\nYou Entered : {Userbowling} \nComputer Entered : {Comp_Bating_function_val} \nTotal : {Comp_Bating_Result} \n" )
                        if Run and Comp_Bating_Result > User_Bating_Result :
                            print("I Won")
                            break
                        continue
                
                


    LD.loading(text = "Loading results.")
    print(f"\nComputer's Run : {Comp_Bating_Result}")
    print(f"Your Run : {User_Bating_Result}")
    if Comp_Bating_Result > User_Bating_Result:
        print("Yes! I won! Hey you did good.")
        re = input("Re-match ? (Hit Enter or any-other to quit.)")
        if re == "":
            isrunning = True
            print("-+"*10, "New Match", "-+"*10)
            continue
        else:
            print("Too scared !")
            isrunning = False
    elif User_Bating_Result > Comp_Bating_Result:
        print("Yay! You won! Hey you did good.")
        re = input("Re-match ? (Hit Enter or any-other to quit.)")
        if re == "":
            LD.loading(text = "Loading Match.")
            print("-+"*10, "New Match", "-+"*10)
            isrunning = True
            continue
        else:
            print("\nToo scared !")
            isrunning = False
            break
    else:
        print("It's a tie.")
        print("Loading Next Match", end = " ")
        LD.loading(text = "")
        print("\n-+"*10, "New Match", "-+"*10)
        continue
        
input()