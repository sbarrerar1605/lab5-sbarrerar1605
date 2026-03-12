def total_steps(steps):
    return sum(steps)


def average_steps(steps):
    return sum(steps) // len(steps)


def max_steps(steps):
    return max(steps)


def min_steps(steps):
    return min(steps)


def goal_met(steps):
    result = []
    for s in steps:
        result.append(s >= 10000)
    return result


user_input = input("Enter your daily steps for 7 days separated by spaces:\n")

steps = list(map(int, user_input.split()))

total = total_steps(steps)
avg = average_steps(steps)
highest = max_steps(steps)
lowest = min_steps(steps)
goals = goal_met(steps)

print(f"Total steps: {total}")
print(f"Average daily steps: {avg}")
print(f"Highest steps in a day: {highest}")
print(f"Lowest steps in a day: {lowest}")
print(f"Goal met each day: {goals}")