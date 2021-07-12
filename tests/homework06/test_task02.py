import pytest

from homework06.task02 import *

opp_teacher = Teacher("Daniil", "Shadrin")
advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

lazy_student = Student("Roman", "Petrov")
good_student = Student("Lev", "Sokolov")

oop_hw = opp_teacher.create_homework("Learn OOP", 1)
docs_hw = opp_teacher.create_homework("Read docs", 5)

result_1 = good_student.do_homework(oop_hw, "I have done this hw")
result_3 = lazy_student.do_homework(docs_hw, "done")

opp_teacher.check_homework(result_1)
temp_1 = opp_teacher.homework_done

advanced_python_teacher.check_homework(result_1)
temp_2 = Teacher.homework_done


def test_HomeworkResult_accepts_only_Homework_object():
    """Testing that error is raised if attribute is not Homework instance"""
    with pytest.raises(AttributeError):
        result4 = HomeworkResult(good_student, "fff", "Solution")


def test_short_solution_not_accepted():
    """Testing check_homework method returns False when solution is less than 5 chars long"""
    assert opp_teacher.check_homework(result_3) == False


def test_homework_dictionary():
    """Testing that checked homeworks are saved to dictionary with unique solutions"""
    assert temp_1 == temp_2


def test_solutions_are_saved_to_dictionary():
    """Testing slutions are reached from dictionary by homework object"""
    assert Teacher.homework_done[oop_hw] == {result_1}


def test_reset_results():
    """Testing that result are cleared after reset"""
    Teacher.reset_results()
    assert Teacher.homework_done == {}
