from utils import flip, count_letters

message = input("Please type your message\n")

flipped = flip(message)
count_a = count_letters(message, 'a')

encoded = flipped + str(count_a)

print(f"Your encoded message is: {encoded}")