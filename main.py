import random

# counters for record
compWins = 0
userWins = 0
draws = 0

options = ["Rock", "Paper", "Scissors"]

# user's choice

while 1:
    while 1:
        try:
            userNum = int(input("Choose one:\n'1' : Rock\n'2' : Paper\n'3' : Scissors\n'0' : Exit\n")) - 1
            # end the program
            if userNum == -1:
                exit()

            userOption = options[userNum]
            print("Your choice: "+userOption)
            break

        except IndexError:
            print("Please choose a number from 0-3.")
        except ValueError:
            print("Please enter an integer.")
        except Exception:
            print("Please enter a valid number.")



    # computer's choice
    compOption = random.choice(options)
    print("Computer's choice: "+compOption)


    # print who won and the record
    if userOption == compOption:
        print("It's a tie!")
        draws += 1
    elif userOption == "Rock":
        if compOption == "Paper":
            print("Computer wins!")
            compWins += 1
        else:
            print("You win!")
            userWins += 1
    elif userOption == "Paper":
        if compOption == "Rock":
            print("You win!")
            userWins += 1
        else:
            print("Computer wins!")
            compWins += 1
    elif userOption == "Scissors":
        if compOption == "Rock":
            print("Computer wins!")
            compWins += 1
        else:
            print("You win!")
            userWins += 1

    print("Current record: You: "+str(userWins) + " Comp: "+str(compWins)+" Draws: "+str(draws))