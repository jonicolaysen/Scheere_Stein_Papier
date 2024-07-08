import random,sys

userWin = 0
computerWin = 0


print("Challenge yourself to a game of rock-paper-scissors!")
for i in range(0,5):

    print("please choose: Scissors(s), Rock(r), Paper(p)")

    userInput = input("your choice: ")

    answers = ["s","p","r"]
    if userInput not in answers:
        print("error")
        sys.exit(1)
    random.shuffle(answers)
    computerInput = answers[0]
    print("computer: "+ computerInput)    

    if computerInput == userInput:
        print ("Tie")
    if computerInput == "s" and userInput == "p":
        print ("you lost!")
        computerWin+=1
    if computerInput == "s" and userInput == "r":
        print ("you won!")
        userWin+=1
    if computerInput == "r" and userInput == "s":
        print ("you lost!")
        computerWin+=1
    if computerInput == "r" and userInput == "p":
        print ("you won!")
        userWin+=1
    if computerInput == "p" and userInput == "r":
        print ("you lost!") 
        computerWin+=1
    if computerInput == "p" and userInput == "s":
        print ("you won!")
        userWin+=1

if userWin > computerWin: 
    print ("You´ve won the Tournament!!!")
if computerWin > userWin:
    print ("You´ve lost the tournament!!!")
if computerWin == userWin:
    print ("Tie")

print (f"User Score = {userWin}")
print (f"Computer Score = {computerWin}")
        

