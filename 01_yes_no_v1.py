
show_instructions = ""

while show_instructions != "end":
    
    # ask user if played before

    show_instructions = input("have you played before? ")

    # response to users input

    if show_instructions == "yes":
        print("continue to game")
        show_instructions = "end"
    elif show_instructions == "y":
        print("continue to game")
        show_instructions = "end"

    elif show_instructions == "no":
        print("show intro")
        show_instructions = "end"
    elif show_instructions == "n":
        print("show intro")
        show_instructions = "end"

    else:
        print("you must enter either yes or no")

