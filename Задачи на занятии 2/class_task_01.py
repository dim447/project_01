# Задача 1
# Приведем список покупок в магазине

shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']

# Измените список согласно пунктам задания
# Выведите результат каждого пункта на консоль по очереди

#   а. Вставьте рыбу между горошком и рисом
#   b. Добавьте фрукты из списка fruits в конец списка shop_list

fruits = ['Яблоко', 'Апельсин', 'Клубника']

#   c. Удалите из списка shop_list картофель
#   d. Какими по счету стоят хлеб и апельсин? Выведите номера на консоль в формате
#   Номер "продукта" в списке - N 

shop_list.insert(2, 'Рыба')
print(shop_list)
shop_list += fruits
print(shop_list)
shop_list.remove('Картофель')
print(shop_list)
print(f"Номер продукта -Хлеб- в списке {shop_list.index('Хлеб')}\nНомер продукта -Апельсин- в списке {shop_list.index('Апельсин')}")
