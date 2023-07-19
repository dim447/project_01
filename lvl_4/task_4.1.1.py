import sqlite3 as sq

tuple_of_teacher = ((101, 'Галина', 1, '2021-2-10', 'Физик', 40000, 0),
                    (102, 'Мария', 1, '2018-07-23', 'Химик', 20000, 0),
                    (103, 'Ольга', 2, '2022-05-19', 'Информатик', 25000, 0),
                    (104, 'Полина', 2, '2017-12-28', 'Физик ', 28000, 0),
                    (105, 'Лидия', 3, '2015-06-04', 'Информатик', 42000, 0),
                    (106, 'Анастасия', 3, '2019-09-11', 'Учитель трудов', 30000, 0),
                    (107, 'Ирина', 4, '2020-08-21', 'Информатик', 32000, 0),
                    (108, 'Виктория', 4, '2017-10-17', 'Географ', 30000, 0))

tuple_of_school = ((1, 'Протон', 200),
                   (2, 'Перспектива', 300),
                   (3, 'Спектр', 400),
                   (4, 'Содружество', 500))


def on_startup():
    sql_start()


def sql_start():
    global base_connect, cur
    base_connect = sq.connect("/Users/idim/PycharmProjects/project_01/lvl_4/teachers1.db")
    cur = base_connect.cursor()
    if base_connect:
        pass
        # print('Data base connected Ok!')
    base_connect.execute(
        'CREATE TABLE IF NOT EXISTS School (School_Id INTEGER NOT NULL PRIMARY KEY, School_Name TEXT NOT NULL, Place_Count INTEGER NOT NULL)')
    base_connect.execute(
        'CREATE TABLE IF NOT EXISTS Teacher (Teacher_Id INTEGER NOT NULL PRIMARY KEY, Teacher_Name TEXT NOT NULL, School_Id INTEGER '
        'NOT NULL, Joining_Date TEXT NOT NULL, Speciality TEXT NOT NULL, Salary INTEGER NOT NULL, Experience INTEGER)'
                        )
    base_connect.commit()
    base_connect.close()


def sql_add_teacher(data):
    cur.execute('INSERT INTO Teacher (Teacher_Id, Teacher_Name, School_id, Joining_Date, '
                'Speciality, Salary, Experience) VALUES (?,?,?,?,?,?,?)', tuple(data))
    base_connect.commit()
    base_connect.close()


def sql_add_school(data):
    cur.execute('INSERT INTO School (School_Id, School_Name, Place_Count) VALUES (?,?,?)', tuple(data))
    base_connect.commit()
    base_connect.close()


def read_teacher_by_school(num):
    ret = cur.execute('SELECT * FROM Teacher WHERE School_id == ?', [num]).fetchall()
    for _ in ret:
        print(f'➢ ID Учителя: {_[0]}\n➢ Имя Учителя: {_[1]}\n➢ ID школы: {_[2]}\n'
              f'➢ Дата начала работы: {_[3]}\n➢ Специализация: {_[4]}\n➢ Зарплата: {_[5]}\n'
              f'➢ Опыт работы: {_[6]}\n')


def sql_read_teacher(number):
#     # ret = cur.execute('SELECT * FROM students ORDER BY RANDOM() LIMIT 1').fetchone()
#     # ret = cur.fetchone()
#     # # ret = cur.execute('SELECT * FROM table ORDER BY RANDOM() LIMIT 1')
    ret = cur.execute('SELECT * FROM Teacher WHERE Teacher_Id =?', [number]).fetchone()
    print(f'➢ ID Учителя: {ret[0]}\n➢ Имя Учителя: {ret[1]}\n➢ ID школы: {ret[2]}\n'
          f'➢ Дата начала работы: {ret[3]}\n➢ Специализация: {ret[4]}\n➢ Зарплата: {ret[5]}\n'
          f'➢ Опыт работы: {ret[6]}\n')
    base_connect.commit()


def read_all_teachers():
    ret = cur.execute('SELECT * FROM Teacher').fetchall()
    for _ in ret:
        print(f'➢ ID Учителя: {_[0]}\n➢ Имя Учителя: {_[1]}\n➢ ID школы: {_[2]}\n'
              f'➢ Дата начала работы: {_[3]}\n➢ Специализация: {_[4]}\n➢ Зарплата: {_[5]}\n'
              f'➢ Опыт работы: {_[6]}\n')


def read_all_school():
    ret = cur.execute('SELECT * FROM School').fetchall()
    for _ in ret:
        print(f'➢ ID школы: {_[0]}\n➢ Название школы: {_[1]}\n➢ Количество мест: {_[2]}\n')


def sql_delete_teacher(data):
    cur.execute('DELETE FROM Teacher WHERE Teacher_Name == ?', (data,))
    base_connect.commit()


def close_connection(base_connect):
    if base_connect:
        base_connect.close()


##############################################################
if __name__ == '__main__':
    on_startup()
    # for i in range(len(tuple_of_teacher)):
    #     sql_add_teacher((tuple_of_teacher[i][0], tuple_of_teacher[i][1], tuple_of_teacher[i][2], tuple_of_teacher[i][3],
    #                      tuple_of_teacher[i][4], tuple_of_teacher[i][5], tuple_of_teacher[i][6]))
    # for _ in range(len(tuple_of_school)):
    #     sql_add_school((tuple_of_school[_][0], tuple_of_school[_][1], tuple_of_school[_][2]))
    # cur.execute('UPDATE Teacher SET Experience == ?', (200,))
    # sql_read_teacher(107)
    # read_all_school()
    read_all_teachers()
    # sql_add_teacher((110, 'Игоревна', 4, '1917-10-17', 'Директор', 130000, 1000))
    # read_teacher_by_school(3)
    # base_connect.commit()

##############################################################