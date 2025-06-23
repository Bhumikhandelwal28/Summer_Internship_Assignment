import random
choices=["Rock","Paper","Scissor"]
print("---Welcome to Rock paper scissor game---")
n=int(input("Enter the number of turns you want to play"))
uscore=0
cscore=0
count=0
while count<n:
    uchoice = input(""" Enter from any of these
    1.Rock
    2.Paper
    3.Scissor
    4.Exit
    """).capitalize()
    if uchoice=="exit":
        print("Thanks for playing")
        break
    if uchoice not in choices:
        print("Invalid Choice")
        continue
    cchoice=random.choice(choices)
    print("The computer choose: ",cchoice)
    if uchoice==cchoice:
        print("There is a tie")
        uscore+=1
        cscore+=1
    elif (
        (uchoice == "rock" and cchoice == "scissors") or
        (uchoice == "paper" and cchoice == "rock") or
        (uchoice == "scissors" and cchoice == "paper")
        ):
        print("You win!")
        uscore+=1
    else:
        print("Computer wins!")
        cscore+=1
    count+=1

    print("Your Scores are:")
    print("User score:",uscore)
    print("Computer score:",cscore)

if uscore<cscore:
    print("The Winner of the game is Computer")
elif uscore==cscore:
    print("The Winner of the game is User and Computer both")
else:
    print("The Winner of the game is User")

print("Thanks for playing")