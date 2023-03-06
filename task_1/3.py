# Напишіть програму на Python щоб отримати рядок із перших 2 і останніх 2 символів заданного рядка. Якщо довжина рядка
# менше 2, викличте виняток
# Write a Python program to get a string from the first 2 and last 2 characters of a given string. If the length of the
# string is less than 2, throw an exception
# Bazdyriev Lev

if __name__ == '__main__':
    str = input("Please enter a string: ")
    if len(str) < 2:
        raise Exception("The line is less than two characters")
    print(f"{str[:2]}{str[len(str) - 2:]}")
