# Задача 7
# Проверьте, содержит ли строка одинаковое количество "x" и "o".
# Функция должна возвращать логическое значение и быть нечувствительным к регистру. 
# Строка может содержать любые символы.

# Примеры ввода/вывода:
#   XO("ooxx") => true
#   XO("xooxx") => false
#   XO("ooxXm") => true
#   XO("zpzpzpp") => true # когда нет "x" и "o", должно быть возвращено значение true
#   XO("zzoo") => false


def xo(string):
    j, i = 0, 0
    string = string.lower()
    j = string.count('x')
    i = string.count('o')
    if i != j:
        print(False)
    elif i == 0 and j == 0:
        print(True)
    else:
        print(True)


xo("oooXx")
xo("zpzpzpp")
xo("ooxx")
xo("xooxx") 
xo("ooxXm")
xo("zpzpzpp")
xo("zzoo")