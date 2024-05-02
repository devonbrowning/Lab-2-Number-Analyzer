continue_program = True

name = input("Hello! What is your name? ")
print(name + ", welcome to my number analyzer!")

while continue_program:
    try:
        num = int(input("Please enter an integer between 1 and 100 inclusive: "))
        if num < 1 or num > 100:
            print("Please enter a positive integer between 1 and 100.")
            continue

        if num % 2 == 0:
            if 2 <= num <= 24:
                print(f"{num} is even and less than 25.")
            elif 26 <= num <= 60:
                print(f"{num} is even and between 26 and 60 inclusive.")
            else:
                print(f"{num} is even and greater than 60.")
        else:
            if num < 60:
                print(f"{num} is odd and less than 60.")
            else:
                print(f"{num} is odd and greater than 60.")

        choice = input(name + ", do you want to continue? (yes/no): ").lower()
        if choice != "yes":
            continue_program = False
            print("Okay, have a good day " + name + "!")
    except ValueError:
        print("Please enter a valid integer.")





