import datetime

import pytest

from homework06.task02 import *


@pytest.fixture
def teacher():
    return Teacher("Remus", "Lupin")


@pytest.fixture
def student():
    return Student("Lee", "Jordan")


@pytest.fixture
def homework():
    return Homework("Goblin thesis", 7)


def test_Teacher_class_attr(teacher):
    assert teacher.first_name == "Remus"
    assert teacher.last_name == "Lupin"


def test_Student_class_attr(student):
    assert student.first_name == "Lee"
    assert student.last_name == "Jordan"


def test_Student_do_homework(student, homework):
    result = student.do_homework(homework, "Solution to Goblin thesis")
    assert isinstance(result, HomeworkResult)
    assert result.homework == homework
    assert result.solution == "Solution to Goblin thesis"
    assert result.author == student


def test_Student_do_homework_late(student, homework):
    homework.created = datetime.datetime.today() - datetime.timedelta(days=10)
    with pytest.raises(DeadlineError):
        student.do_homework(homework, "Solution to Goblin thesis")


def test_Teacher_create_homework(teacher):
    homework = teacher.create_homework("Boggarts", 5)
    assert isinstance(homework, Homework)
    assert homework.text == "Boggarts"
    assert homework.deadline == datetime.timedelta(days=5)


def test_Teacher_check_homework(teacher, student, homework):
    bad_result = HomeworkResult(student, homework, "done")
    good_result = HomeworkResult(student, homework, "Solution to Goblin thesis")
    assert Teacher.homework_done == {}
    assert not teacher.check_homework(bad_result)
    assert teacher.check_homework(good_result)
    assert Teacher.homework_done[homework] == {good_result}
    Teacher.reset_results()
    assert Teacher.homework_done == {}


def test_wrong_homework_result(student):
    with pytest.raises(AttributeError):
        wrong_result = HomeworkResult(
            student, "not-a-homework", "no-matter-what-solution"
        )
