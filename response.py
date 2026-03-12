def input_response(secret_number, user_input):
    if user_input < secret_number:
        return "Too low! Try a higher number.", False
    elif user_input > secret_number:
        return "Too high! Try a lower number.", False
    else:
        return "Correct! You guessed the number!", True