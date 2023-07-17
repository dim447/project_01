def month(num, lang):
    months_en = ('January', 'Fabruary', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December')
    months_ru = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')
    if lang == 'ru':
        return months_ru[num - 1]
    else:
        return months_en[num - 1]


result = month(1, "en")
print(result)
