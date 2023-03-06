# Напишіть функцію Python, яка приймає ім’я та прізвище користувача та друкує
# їх у зворотному порядку з пробілом між ними
# Write a Python function that accepts both names and others in reverse order with a gap between them
# Bazdyriev Lev

if __name__ == '__main__':
    name = input("Enter is your name: ")
    words = name.split()
    words.reverse()
    print(" ".join(words))
