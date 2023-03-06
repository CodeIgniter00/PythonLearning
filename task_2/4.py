# Напишіть програму на Python для друку календаря заданого місяця та року. Використайте модуль calendar
# Write a Python program for another calendar of a given month and date. Use calendar module
# Bazdyriev Lev

import calendar
from prettytable import PrettyTable

if __name__ == '__main__':
    try:
        year = int(input("Please input the year: "))
        month = int(input("Please input the month: "))
        calendar.setfirstweekday(calendar.MONDAY)
        matrix = calendar.monthcalendar(year, month)
        table_calendar = PrettyTable()
        table_calendar.field_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        table_calendar.add_rows(matrix)
        print(table_calendar)
    except calendar.IllegalMonthError:
        print(f"bad month number {month}; must be 1-12")
