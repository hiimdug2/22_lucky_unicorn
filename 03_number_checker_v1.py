
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
