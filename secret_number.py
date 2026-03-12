import random

def seed_secret_numbers(seed):
    random.seed(seed)

def generate_secret_number(start=1, end=100):
    return random.randint(start, end)