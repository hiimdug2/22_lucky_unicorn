
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


asking = True

while asking:
    show_instructions = yes_no_checker("have you played before ")

    if show_instructions == "yes":
        print("you have chosen not to see the instructions")

    else:
        show_instructions = "no"
        print("you have chosen to see the instructions")

    asking = False
