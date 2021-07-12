"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime


class Homework:
    """Homework task with deadline"""

    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.today()

    def is_active(self):
        return self.created + self.deadline > datetime.datetime.today()


class Student:
    """Student does homework"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework):
        if homework.is_active():
            return homework
        else:
            print("You are late")
            return None


class Teacher:
    """Teacher creates homeworks"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def create_homework(cls, text, days):
        return Homework(text, days)


if __name__ == "__main__":
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    print(f"Teacher's last name is {teacher.last_name} (is it  Shadrin?)")
    print(f"Student's first name is {student.first_name} (is it  Roman?)")

    expired_homework = teacher.create_homework("Learn functions", 0)
    print(f"{expired_homework.created=} (is it Example: 2019-05-26 16:44:30.688762?)")
    print(f"{expired_homework.deadline=} (is it 0:00:00?)")
    print(f"{expired_homework.text=} (is it Learn functions?)")

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    print(f"{oop_homework.deadline=} (is it 5 days, 0:00:00?)")

    print(
        f"{oop_homework.created=}\n{oop_homework.deadline=}\n{datetime.datetime.today()=}"
    )
    print("Now we expect nothing to be printed")
    student.do_homework(oop_homework)
    print("Now we expect 'You are late' to be printed")
    student.do_homework(expired_homework)  # You are late
