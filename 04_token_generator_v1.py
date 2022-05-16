from random import randint


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


wallet = True
play_game = True

while play_game:

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

    continue_game = yes_no_checker("would you like to continue ")

    if continue_game == "yes" and wallet_amount >= 0.5:
        token = randint(1, 10)
        if 1 <= token <= 3:
            print("you got a donkey")
            wallet_amount -= 1
        elif 4 <= token <= 6:
            print("you got a horse")
            wallet_amount -= 0.5
        elif 7 <= token <= 9:
            print("you got a zebra")
            wallet_amount -= 0.5
        elif token == 10:
            print("you got a unicorn")
            wallet_amount += 4
        print(f"you have ${wallet_amount} left ")
    else:
        play_game = False
