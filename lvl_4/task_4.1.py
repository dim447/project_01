# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:
import sqlite3 as sq

# class Students:
#     def __init__(self, student_id, student_name, school_id):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.school_id = school_id
#
#     def __str__(self):
#         return f"Имя студента: {self.student_name} " \
#                f"ID Студента: {self.student_id} " \
#                f"ID школы: {self.school_id}."


# ivan = Students(211, "Костя", 11)
# print(ivan)
list_of_students = [
    [221, 'Sofia', 1],
    [222, 'Adam', 2],
    [223, 'Lisa', 3],
    [224, 'Ignat', 4]
]


def on_startup():
    sql_start()


def sql_start():
    global base_connect, cur
    base_connect = sq.connect("/Users/idim/PycharmProjects/project_01/lvl_4/teachers1.db")
    cur = base_connect.cursor()
    if base_connect:
        # pass
        print('Data base connected Ok!')
    base_connect.execute(
        'CREATE TABLE IF NOT EXISTS students (student_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, student_name TEXT, school_id INTEGER)')
    base_connect.commit()


def sql_add_student(data):  # Добавить студенат в базу
    cur.execute('INSERT INTO students (student_id, student_name, school_id) VALUES (?,?,?)', tuple(data))
    base_connect.commit()


def sql_read_student(number):  # Выввести инфу по студенту по его ID
    ret = cur.execute('SELECT * FROM students where student_id =?', [number]).fetchone()
    print(f'ID Студента: {ret[0]}\nИмя студента: {ret[1]}\nID школы: {ret[2]}')
    base_connect.commit()


def read_all_students():  # Выввести инфу по всем студентам
    ret = cur.execute('SELECT * FROM students').fetchall()
    for _ in ret:
        print(f'ID Студента: {_[0]}\nИмя студента: {_[1]}\nID школы: {_[2]}\n\n')


def get_student_by_student(number):  # Выввести инфу по студенту по его ID JOIN инфу по школе
    ret = cur.execute('SELECT * FROM students '
                      'JOIN School ON School.School_id = students.school_id '
                      'WHERE student_id =?', [number]).fetchone()
    print(f'ID Студента: {ret[0]}\nИмя студента: {ret[1]}\nID школы: {ret[2]}\nНазвание школы: {ret[4]}\n'
          f'Количество мест: {ret[5]}')
    base_connect.commit()


def get_student_with_teacher(number):  # Выввести инфу по студенту по его ID JOIN инфу по учиталям в данной школе
    ret = cur.execute('SELECT * FROM students '
                      'JOIN Teacher ON Teacher.School_id = students.school_id '
                      'WHERE student_id =?', [number]).fetchall()
    print(f'ID Студента: {ret[0][0]}\nИмя студента: {ret[0][1]}\nID школы: {ret[0][2]}\n')
    for _ in range(len(ret)):
        print(f'ID Учителя: {ret[_][3]}\n'
              f'Имя учителя: {ret[_][4]}\n'
              f'Должность учителя: {ret[_][7]}\n')
    base_connect.commit()


def get_student_by_school(number):  # Выввести инфу по студенту по ID школы JOIN инфу по школе
    ret = cur.execute('SELECT * FROM students '
                      'JOIN School ON School.School_id = students.school_id '
                      'WHERE School.School_id =?', [number]).fetchall()
    for _ in ret:
        print(f'ID Студента: {_[0]}\nИмя студента: {_[1]}\nID школы: {_[2]}\nНазвание школы: {_[4]}\n')
    base_connect.commit()


def sql_delete_student(data):  # Удалить студента из базы
    cur.execute('DELETE FROM students WHERE student_name == ?', (data,))
    base_connect.commit()


##############################################################
if __name__ == '__main__':
    on_startup()
    # sql_add_student((206, "Игорь", 4))
    # sql_delete_student("Игорь")
    # for i in range(len(list_of_students)):
    #     name_student = Students(list_of_students[i][0], list_of_students[i][1], list_of_students[i][2])
    #     sql_add_student((name_student.student_id, name_student.student_name, name_student.school_id))
    # read_all_students()
    # sql_read_student(222)
    # get_student_by_student(222)
    # get_student_by_school(4)
    get_student_with_teacher(205)
    base_connect.close()

##############################################################
