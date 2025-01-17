"""

На вход программы поступает целое число — порядковый номер месяца.
Напишите программу, которая выводит построчно название месяца и время года, к которому этот месяц относится.
Название месяца и времени года должны выводится с маленькой буквы.

Если вводимое число не попадает в диапазон [1; 12], программа выводит “ошибка”.
"""

#{{}} this created a dictionary with an empty set
if __name__ == "__main__":
    months = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август",
              9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}
    seasons = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето", 9: "осень",
               10: "осень", 11: "осень", 12: "зима"}
    numberOFMonth = int(input())  # we have the input from the user
    if numberOFMonth > 12 or numberOFMonth < 1:
        print("ошибка")
    else:
        print(months[numberOFMonth])
        print(seasons[numberOFMonth])
