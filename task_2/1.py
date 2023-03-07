# Напишіть функцію Python, яка приймає радіус кола від користувача та обчислює площу
# Write a Python function that accepts the user circle radius and calculates the area
# Bazdyriev Lev

import math

if __name__ == '__main__':
    try:
        radius: float = float(input("Input circle radius: "))
        S = round(math.pi * math.pow(radius, 2), 2)
        print(f"S = {S}")
    except ValueError:
        print("You didn't enter a number")
