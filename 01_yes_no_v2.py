
looping = True

while looping:

    show_instructions = input("have you played before ").lower().strip()

    if show_instructions == "yes" or show_instructions == "y":
        print("continue to game")
        looping = False

    elif show_instructions == "no" or show_instructions == "n":
        print("show instructions")
        looping = False

    else:
        print("you must enter either yes or no")
