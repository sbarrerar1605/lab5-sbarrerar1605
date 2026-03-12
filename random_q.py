import random

random.seed(123)

start = int(input("Enter the start value:\n"))
end = int(input("Enter the end value:\n"))

num = random.randint(start, end)

print(f"Generated random number: {num}")