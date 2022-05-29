import random

# main routine

starting_balance = 100
balance = starting_balance

# generates and enacts tokens
for item in range(0, 100):
    chosen_num = random.randint(1, 100)

    # adjust balance
    if 1 <= chosen_num <= 5:
        balance += 4
        chosen = "unicorn"
    if 6 <= chosen_num <= 36:
        balance -= 1
        chosen = "donkey"
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
        balance -= 0.5

    # output
    print(f"token: {chosen}, balance: ${balance}")

print(f"starting balance: ${starting_balance}")
print(f"final balance: ${balance}")
