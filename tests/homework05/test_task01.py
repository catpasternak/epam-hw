import datetime

import pytest

from homework05.task01 import Homework, Student, Teacher

homework_testdata = [("homework-1", 10, True), ("homework-2", 0, False)]


@pytest.mark.parametrize("text, deadline, status", homework_testdata)
def test_homework_class_attributes(text, deadline, status):
    """Testing Homework class"""
    homework = Homework(text, deadline)
    created = datetime.datetime.today()
    assert homework.text == text
    assert homework.deadline == datetime.timedelta(days=deadline)
    assert created - homework.created < datetime.timedelta(seconds=1)
    assert homework.is_active() == status


homework1, homework2 = Homework("homework-1", 10), Homework("homework-2", 0)
student_testdata = [
    ("Jimi", "Hendrix", homework1, homework1),
    ("Keith", "Richards", homework2, None),
]


@pytest.mark.parametrize("first_name, last_name, homework, expected", student_testdata)
def test_student_class_attributes_and_methods(
    first_name, last_name, homework, expected
):
    """Testing Student class"""
    student = Student(first_name, last_name)
    homework_result = student.do_homework(homework)
    assert student.first_name == first_name
    assert student.last_name == last_name
    assert homework_result == expected


teacher_testdata = [("Chuck", "Berry", "homework-3", 7)]


@pytest.mark.parametrize("first_name, last_name, text, deadline", teacher_testdata)
def test_teacher_class_attributes_and_methods(first_name, last_name, text, deadline):
    """Testing Teacher class and @classmethod function"""
    teacher = Teacher(first_name, last_name)
    homework_func = teacher.create_homework
    homework = homework_func(text, deadline)
    assert teacher.first_name == first_name
    assert teacher.last_name == last_name
    assert homework.text == text
    assert homework.deadline == datetime.timedelta(days=deadline)
