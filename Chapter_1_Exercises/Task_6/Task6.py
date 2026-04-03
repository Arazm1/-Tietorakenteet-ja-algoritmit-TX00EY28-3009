total_counter = 0

while True:

    user_input = input();

    if(user_input == "0"):
        break

    try:
        total_counter += int(user_input)
        print(f"The total is now {float(total_counter)}")

    except ValueError:
        print("That wasn’t a number.")


print(f"The grand total is {float(total_counter)}")