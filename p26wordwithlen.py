print("This is a program to print words of a sentence and their length.")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

sentence = input("Enter a sentence : ")
List = sentence.split()
print(f"There {len(List)} words in the sentence.")
for i in List:
    print(f"{i} --> {len(i)}")

input()