class Student:
    def __init__(self, fname, age, sex):
        self.name = fname
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"Студент: {self.name} --> " \
               f"возраст: {self.age} лет --> " \
               f"пол: {self.sex}."


class Student_man(Student):
    def __init__(self, sex, fname, age):
        super().__init__(fname, age, sex)
        self.sex = 'man'


with open('final.txt', 'r') as f:
    name = f.readlines()


# новая правка для junior Это правка в junior
def hello(text):
    print(text)


if __name__ == '__main__':
    student = Student_man(fname=name[0].rstrip('\n'), age=55, sex='')
    student1 = Student(fname=name[1].rstrip('\n'), age=45, sex='woman')
    hello(student)
    hello(student1)
