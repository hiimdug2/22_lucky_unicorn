
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
    print("you can pay an amount up to $10 to start, and each round costs $1. \nafter you pay you will be given a token, either a unicorn, a zebra, a horse, or a donkey.\nif you get unicorn, you win $5, if you get a horse or a zebra, you win $0.50,\nand if you get a donkey, you don't win any money back. \nthe game ends after you lose all your money or quit. ")


if show_instructions == "yes":
    instructions()
else:
    print("then lets get on to the game ")
