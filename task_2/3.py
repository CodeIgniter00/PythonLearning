# Напишіть функцію Python, яка приймає ціле число (n) і обчислює значення n+nn+nnn
# Write a Python function that accepts a number (n) and evaluates the value n+nn+nnn
# Bazdyriev Lev

import math

if __name__ == '__main__':
    try:
        number = int(input("Please enter a number: "))
        value = number + math.pow(number, 2) + math.pow(number, 3)
        print(f"Value = {value}")
    except ValueError:
        print("You didn't enter a number")
