print('Задача 5. Наибольшая сумма цифр\n')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

num_count = int(input("Количество чисел: "))

result_num = 0
result_sum = 0

for _ in range(num_count):
    user_input = input("Введите число: ")
    current_sum = 0

    for digit in user_input:
        current_sum += int(digit)

    result_sum = max(result_sum, current_sum)
    result_num = user_input if current_sum == result_sum else result_num

print(f"\nНаибольшее по сумме цифр число: {result_num} (сумма цифр: {result_sum})")
