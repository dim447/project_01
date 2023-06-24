# Простенький файл приветствие берёт имя и фамилию из файла final.txt и печатает 
class Student:
    def __init__(self, fname, age, sex):
        self.name = fname
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"Студент: {self.name} --> " \
               f"возраст: {self.age} лет --> " \
               f"пол: {self.sex}."


class StudentMan(Student):
    def __init__(self, sex, fname, age):
        super().__init__(fname, age, sex)
        self.sex = 'man'


with open('final.txt', 'r', encoding='utf-8') as f:
    name = f.readlines()


def hello(text):
    print(f'Добрый день! \n{text}')


if __name__ == '__main__':
    student = StudentMan(fname=name[0].rstrip('\n'), age=55, sex='')
    hello(student)
