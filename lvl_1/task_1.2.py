# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import random
import datetime


my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

random_my_favorite_songs = random.choices(my_favorite_songs, k=3)
print(random_my_favorite_songs)
sum_time = 0
for i in random_my_favorite_songs:
    sum_time += i[1]
sum_time_dec = (sum_time - int(sum_time))
if sum_time_dec > 0.59:
    minutes = sum_time_dec * 100 // 60
    seconds = sum_time_dec - 0.60
    sum_time = int(sum_time) + minutes + seconds

print(f'Три песни звучат {round(sum_time, 2)} минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

random_my_favorite_songs = random.choices(my_favorite_songs, k=3)
print(random_my_favorite_songs)
sum_time = 0
for i in random_my_favorite_songs:
    sum_time += i[1]
sum_time_dec = (sum_time - int(sum_time))
if sum_time_dec > 0.59:
    minutes = sum_time_dec * 100 // 60
    seconds = sum_time_dec - 0.60
    sum_time = int(sum_time) + minutes + seconds

print(f'Три песни звучат {round(sum_time, 2)} минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

random_my_favorite_songs = random.choices(my_favorite_songs, k=3)
print(random_my_favorite_songs)
sum_time = 0
for i in random_my_favorite_songs:
    sum_time += i[1]
seconds = (int(sum_time) * 60) + (sum_time - int(sum_time)) * 100
time_songs = str(datetime.timedelta(seconds=seconds))

print(f'Три песни звучат {time_songs}')
