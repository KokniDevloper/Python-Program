import random

def main():
    print("Welcome to the Dice Roller!")
    print("This program will roll a specified number of dice and display the results.")
    totaldice = int(input("How many dice do you want to roll? "))
    print(f"Rolling {totaldice} dice...")
    print("Each die have 6 sides.")
    totalvalue = 0
    for i in range(totaldice):
        dice = random.randint(1, 6)
        print(f"Dice {i + 1}: {dice}")
        totalvalue += dice
    print(f"Total value of all dice: {totalvalue}")

    if __name__ == "__main__":
        main()