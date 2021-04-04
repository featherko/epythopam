import pytest

from homework.hw6.task2_oop2 import DeadlineError, HomeworkResult, NotHomework
from homework.hw6.task2_oop2 import Student, Teacher


opp_teacher = Teacher("Daniil", "Shadrin")
advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

lazy_student = Student("Roman", "Petrov")
good_student = Student("Lev", "Sokolov")

oop_hw = opp_teacher.create_homework("Learn OOP", 1)
docs_hw = opp_teacher.create_homework("Read docs", 5)

result_1 = good_student.do_homework(oop_hw, "I have done this hw")
result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
result_3 = lazy_student.do_homework(docs_hw, "done")


def test_check_same_result():
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)


@pytest.mark.xfail(raises=NotHomework)
def test_nothomework_exception():
    HomeworkResult(good_student, "asdf", "asdffff")


@pytest.mark.xfail(raises=DeadlineError)
def test_deadline_exception():
    test = opp_teacher.create_homework("test", -1)
    lazy_student.do_homework(test, "test")


def test_reset_results():
    test_hw = Teacher.create_homework("hw", 1)
    res = good_student.do_homework(test_hw, "test>5")
    Teacher.check_homework(res)

    assert test_hw in Teacher.homework_done
    assert res in advanced_python_teacher.homework_done[test_hw]
    Teacher.reset_results(test_hw)

    assert test_hw not in opp_teacher.homework_done
    assert res not in Teacher.homework_done[test_hw]

    Teacher.reset_results()

    assert Teacher.homework_done is not True


def test_check_homework_no_dupl():
    test_hw = Teacher.create_homework("hw", 1)
    res = good_student.do_homework(test_hw, "test>5")
    Teacher.check_homework(res)
    Teacher.check_homework(res)
    Teacher.check_homework(res)

    assert len(Teacher.homework_done[test_hw]) == 1
