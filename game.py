import random

def main():
    print("Hello")
    print("Welcome to Rock Paper and Scissor Game")
    print("Lets Begin")
    print("(You can Exit the game by entering 0)")
    player_ans = player_ans_function()
    while player_ans != 0:
        bot_ans = bot_logic()
        winner(player_ans,bot_ans)
        player_ans = player_ans_function()
    print("Thanks for playing")
 
def player_ans_function():
    player_ans = input("Enter your choice: \nFor Rock: Enter 1\nFor Paper: Enter 2\nFor Scissor: Enter 3\nYOUR CHOICE: ")
    player_ans = validator(player_ans)
    return player_ans

def bot_logic():
    bot_ans= random.randint(1, 3)
    if bot_ans == 1:
        return 1
    elif bot_ans == 2:
        return 2
    else:
        return 3
    
def winner(player_ans, bot_ans):

    #Linking player input with Answer
    if player_ans == 1:
        player_answer = "Rock"
    elif player_ans == 2:
        player_answer = "Paper"
    else:
        player_answer = "Scissor"

    #Linking player input with Answer
    if bot_ans == 1:
        bot_answer = "Rock"
    elif bot_ans == 2:
        bot_answer = "Paper"
    else:
        bot_answer = "Scissor"


    print("\n\nYour Choice:",player_answer)
    print("Bot Choice:",bot_answer)
    if player_ans == bot_ans:
        print("Tie")
    elif player_ans == 1:
        if bot_ans == 2:
            print("Bot Wins")
        else:
            print("Player Wins")
    elif player_ans == 2:
        if bot_ans == 1:
            print("Player Wins")
        else:
            print("Bot Wins")
    else:
        if bot_ans == 1:
            print("Bot Wins")
        else:
            print("Player Wins")
    print("\n\n----------------------------------------------\n\n")


def validator(ans):
    if ans in ("0", "1", "2", "3"):
        return int(ans)
    else:
        print("\nInvalid Input")
        print("Please Enter Valid Number Only")
        print("Please Try Again\n")
        return player_ans_function()

if __name__ == "__main__":
    main()