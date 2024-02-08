print ("This a program to arange stars")
class StarArangement ():
    
    def ArangeStars (self,_initialnofcolumn,_finalnofcolumn,_symboltouse):
        for i in range (_initialnofcolumn - 1,_finalnofcolumn):       
            for j in range (0, i+1):
                print (_symboltouse , end =(""))
            print ("")    

obj = StarArangement()
obj.ArangeStars(int(input("Enter the initial no. of column : ")),int(input("Enter the final no. of column : ")),input("Enter the symbol to print : "))
input()









