# Напишіть програму Python, щоб отримати один рядок із двох заданих рядків, розділених пробілом, і поміняти місцями
# перші два символи кожного рядка
# Write a Python program to get one row of two specified rows separated by space and change places the first two
# characters of each line
# Bazdyriev Lev

if __name__ == '__main__':
    str_first = input("Input first string: ")
    str_second = input("Input second string: ")

    str_first = str_first[1] + str_first[0] + str_first[2:]
    str_second = str_second[1] + str_second[0] + str_second[2:]
    print(f"{str_first} {str_second}")
