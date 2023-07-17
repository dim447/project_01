# def even_digit_sum(numbers):
#     new_lst = []
#     for number in numbers:
#         # Преобразуем число в строку
#         number_str = str(number)
#
#         # Инициализируем переменную для хранения суммы
#         sum = 0
#         # Перебираем все символы в строке
#         for digit in number_str:
#             # Преобразуем символ обратно в число
#             sum += int(digit)
#
#             # Проверяем, является ли число чётным
#         if sum % 2 == 0:
#             new_lst.append(number)
#
#     return new_lst

    # # Возвращаем полученную сумму
    # return sum

# even_digit_sum = lambda numbers: [number for number in numbers for digit in str(number) if sum(digit) % 2 == 0]
even_digit_sum = lambda numbers: [number for number in numbers if sum(int(digit) for digit in str(number)) % 2 == 0]
# Пример использования функции
arr = (32, 64, 128, 256, 512)
result = even_digit_sum(arr)
print(f"Чётная сумма цифр числа равна {result}")


# even_digit_sum = lambda numbers: sum(int(digit) for number in numbers for digit in str(number) if int(digit) % 2 == 0)

