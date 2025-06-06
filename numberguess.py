import random

def main():
    print("Welcome to the Number Guessing Game!")
    winner_num = num_range()
    guess(winner_num)


def num_range():
    print("Enter the range of numbers you want to guess from: ")
    num1 = int(input("Enter the Minimum Number from where you want to Begin: "))
    num2 = int(input("Enter the Maximum Number from where you want to End: "))
    if num1>num2:
        print("\nMinimum number cannot be greater than Maximum number\nPlease Try Again\n")
        return num_range()
    else:
        winner_num = random.randint(num1,num2)
        print(f"A number has been choosed between {num1} and {num2}\nGood Luck Gussing it")
        return winner_num
    

def guess(winner_num):
    total_input = 0
    while True:
        user_input = int(input("Enter your Guess: "))
        total_input += 1
        if user_input == winner_num:
            print("You WON")
            print(f"You Guessed it Right in {total_input} guesses")
            break
        elif user_input > winner_num:
            diff = user_input - winner_num
            if diff >= 100:
                print("Too High")
            elif diff >= 11:
                print("Try Lower Number")
            else:
                print("Try a Little Bit Lower Number")

        else:
            diff = winner_num - user_input
            if diff >= 100:
                print("Too Low")
            elif diff >= 11:
                print("Try Higher Number")
            else:
                print("Try a Little Bit Higher Number")




if __name__ == "__main__":
    main()