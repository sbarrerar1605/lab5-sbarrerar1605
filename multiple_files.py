from utils import flip, count_letters

msg = input("Please type your message: ")

reversed_msg = flip(msg)

count = count_letters(msg, "a")

print(f"Your encoded message is: {reversed_msg}{count}")