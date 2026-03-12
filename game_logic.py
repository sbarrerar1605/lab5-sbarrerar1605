from secret_number import seed_secret_numbers, generate_secret_number
from response import input_response


def main():

    seed = int(input("Enter a seed number: "))
    seed_secret_numbers(seed)

    secret_number = generate_secret_number()

    tries = 0
    correct = False

    while not correct:

        guess = int(input("What is your guess: "))
        tries += 1

        message, correct = input_response(secret_number, guess)
        print(message)

    print(f"It took you {tries} tries!")


if _name_ == "_main_":
    main()