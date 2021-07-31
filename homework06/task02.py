"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    """Exception class. Raised when homework is out of date"""

    pass


class Homework:
    """Homework task, consists of text and deadline. Keeps time of creation.
    Has a check for not exceeding deadline.
    :param text: text of a task
    :type text: str
    :param deadline: number of days for passing solution to homework
    :type deadline: int
    """
    def __init__(self, text, deadline):
        """Constructor method. Introduces `self.created` variable that registers
        time when homework object was created
        """
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.today()

    def is_active(self):
        """Checks if homework hasn't exceeded deadline. Compares moment
        of creation and current date and time.
        :return: True if homeworks hasn't expired, else False
        :rtype: bool
        """
        return self.created + self.deadline > datetime.datetime.today()


class HomeworkResult:
    """Solution to homework.
    :param author: instance of :class:`Student` that did homework
    :type author: :class:`Student`
    :param homework: instance of :class:`Homework` that student did
    :type homework: :class:`Homework`
    :param solution: solution to homework that student wrote
    :type solution: str
    """

    def __init__(self, author, homework, solution):
        """Constructor method."""
        self.author = author
        if not isinstance(homework, Homework):
            raise AttributeError("You gave not a Homework object")
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.today()


class Person:
    """Person has first name and last name.
    :param first_name: first name of person
    :type first_name: str
    :param last_name: last name of person
    :type last_name: str
    """

    def __init__(self, first_name, last_name):
        """Constructor method."""
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    """Student who can do homework.
    """

    def do_homework(self, homework, solution):
        """Checks if homework object is not overdue. If it is not -
        returns that homework result object. Else raises exception with message.
        :param homework: object of :class:`Homework`
        :type homework: type
        :param solution: solution to homework that student wrote
        :type solution: str
        :return: instance of :class:`HomeworkResult`
        :rtype: :class:`HomeworkResult`, None
        """
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError("You are late")


class Teacher(Person):
    """Teacher who can create homework.
    """

    @classmethod
    def create_homework(cls, text, days):
        """Creates object of :class:`Homework`.
        :param text: text of homework task
        :type text: str
        :param days: number of days that is deadline for homework
        :type days: int
        :return: object of :class:`Homework`
        :rtype: type
        """
        return Homework(text, days)

    homework_done = defaultdict(set)

    def check_homework(self, homework_result):
        """Returns `True` if length of solution is more than 5 symbols,
        else False
        :param homework_result: instance of :class:`Homework result`
        :rtype: bool
        """
        if len(homework_result.solution) > 5:
            Teacher.homework_done[homework_result.homework].add(homework_result)
            return True
        return False

    @classmethod
    def reset_results(cls, scope="total"):
        """Clears results of homework done.
        :param scope: Scope of clearing, if total - removes all
        :type scope: str
        :return: None
        """
        if scope == "total":
            Teacher.homework_done.clear()
        else:
            del Teacher.homework_done[scope]


if __name__ == "__main__":
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print("There was an exception here")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
