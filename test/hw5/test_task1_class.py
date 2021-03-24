import datetime
from typing import NoReturn, Optional

import pytest

from homework.hw5.task1_class import Homework, Student, Teacher


@pytest.mark.parametrize(("name", "last_name"), [("Pikachu", "Petrov")])
def test_teacher_name_lastname(name: str, last_name: str) -> Optional[NoReturn]:
    teacher = Teacher(last_name, name)

    assert teacher.last_name == last_name
    assert teacher.first_name == name


@pytest.mark.parametrize(("name", "last_name"), [("Sonic", "TheFlash")])
def test_student_name_lastname(name: str, last_name: str) -> Optional[NoReturn]:
    student = Teacher(last_name, name)

    assert student.last_name == last_name
    assert student.first_name == name


def test_homework():
    none_work = Homework("test", 0)
    done_work = Homework("test", 2)
    none_work.created = datetime.datetime.today() - datetime.timedelta(1)
    done_work.created = datetime.datetime.today() - datetime.timedelta(1)

    assert Student.do_homework(none_work) is None
    assert Student.do_homework(done_work) == done_work
