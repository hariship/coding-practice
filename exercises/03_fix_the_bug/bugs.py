# Each function below has ONE bug.
# The comment above each function says what it is supposed to do.
# Fix the code so it does that. Don't change the function names.


# Return a list of the numbers from 1 up to n, including n.
# count_to(3) should give [1, 2, 3]
def count_to(n):
    numbers = []
    for i in range(1, n):
        numbers.append(i)
    return numbers


# Return True if someone of this age can vote (18 or older), otherwise False.
def can_vote(age):
    if age > 18:
        return True
    return False


# a and b are numbers typed in by a user, so they arrive as text, like "5".
# Return their sum as a number. add_typed("5", "3") should give 8
def add_typed(a, b):
    return a + b


# Return the average of a list of numbers.
# average([2, 4, 6, 8]) should give 5
def average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / 3


# hour is 0 to 23. Return "morning" before 12, "afternoon" before 18,
# and "evening" after that.
def greeting(hour):
    if hour < 18:
        return "afternoon"
    elif hour < 12:
        return "morning"
    else:
        return "evening"


# Return the total of all the prices in the list.
# total_price([100, 250, 50]) should give 400
def total_price(prices):
    total = 0
    for p in prices:
        total = total + p
        return total
