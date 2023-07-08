# Задача 6
# Напишите функцию, которая принимает строку в качестве параметра и переворачивает каждое слово в строке. 
# Все пробелы в строке должны быть сохранены.

# Например:
#   "This is an example!" ==> "sihT si na !elpmaxe"
#   "double  spaces"      ==> "elbuod  secaps"

def string_over(string: str):
    new_lst = []
    lst = string.split(' ')
    for i in lst:
        new_lst.append(i[:: -1])
    print(' '.join(new_lst))


string_over("This is an example!")
string_over("double  spaces")
