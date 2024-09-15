print('Задача 7. Пирамидка 2\n')

# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

levels = int(input("Введите количество уровней пирамиды: "))

current_num = 1

for i in range(levels):
    for j in range(2 * levels - 1):
        is_empty_cell = i % 2 == j % 2 if levels % 2 == 0 else i % 2 != j % 2
        end = " " if j < 2 * (levels - 1) else ""

        if is_empty_cell or j < levels - 1 - i or j > levels - 1 + i:
            print(f"{" ":2}", end=end)
        else:
            print(f"{current_num:<2}", end=end)
            current_num += 2
    print()
