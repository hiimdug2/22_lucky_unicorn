
def yes_no_checker(question):

    looping = True

    while looping:
        response = input(question).lower().strip()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("you must enter either yes or no")


show_instructions = yes_no_checker("do you want to see the instructions ")
print(f"you chose {show_instructions}")


def instructions():
    print("you can pay an amount up to $10 to start, and each round costs $1. \n"
          "after you pay you will be given a token, either a unicorn, a zebra, a horse, or a donkey.\n"
          "if you get unicorn, you win $5, if you get a horse or a zebra, you win $0.50,\n"
          "and if you get a donkey, you don't win any money back. \n"
          "the game ends after you lose all your money or quit. ")


if show_instructions == "yes":
    instructions()
else:
    print("then lets get on to the game ")

wallet = True

while wallet:

    try:
        wallet_amount = int(input("how much money would you like to start with, up to $10 "))

        if wallet_amount <= 0 or wallet_amount >= 11:
            print("you must enter a number between 1 and 10")
        else:
            correct_checker = yes_no_checker(f"are you sure you would like to input ${wallet_amount} ")
            if correct_checker == "yes":
                wallet = False
    except ValueError:
        print("you must enter a number between 1 and 10")
