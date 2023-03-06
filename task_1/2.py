# Напишіть програму Python для підрахунку кількості символів (частоти символів) у рядку
# Write a Python program to count the number of characters (character frequency) in a string
# Bazdyriev Lev

def get_frequency(str):
    char_counts = {}
    for char in str:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


if __name__ == '__main__':
    str = input("Please enter a string: ")
    char_list = get_frequency(str)
    for char, count in char_list.items():
        print(f"{char} = {count}")
