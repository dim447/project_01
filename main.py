class Student:
    def __init__(self, fname, age, sex):
        self.name = fname
        self.age = age
        self.sex = sex


class Student_man(Student):
    def __init__(self, sex, fname, age):
        super().__init__(fname, age, sex)
        self.sex = 'man'


with open('final.txt', 'r') as f:
    name = f.read()


def hello(text):
    print(f'Привет, {text}, с началом учёбы!')


if __name__ == '__main__':
    hello(name)

    student = Student_man(fname=name, age=55, sex='')
    student1 = Student(fname=name, age=55, sex='woman')
    print(f'Студент: {student.name}, возраст: {student.age}, пол: {student.sex}')
    print(f'Студент: {student1.name}, возраст: {student1.age}, пол: {student1.sex}')

