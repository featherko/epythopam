"""Task 2.

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
from typing import NoReturn, Optional, Type, TypeVar, Union

T = TypeVar("T")


class NotHomework(Exception):
    """Exception raised when you put non-Homework object."""

    def __init__(self, message: str = "You gave not a homework object"):
        self.message = message
        super().__init__(self.message)


class DeadlineError(Exception):
    """Exception raised when you are late."""

    def __init__(self, message: str = "You are late"):
        self.message = message
        super().__init__(self.message)


class Person:
    """Person."""

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name


class Homework:
    """Homework."""

    def __init__(self, text: str, deadline: int):
        self.text = text
        self.created = datetime.datetime.today()
        self.deadline = datetime.timedelta(deadline)

    def is_active(self) -> bool:
        """Active.

        Checks if this homework is still legitimate to do. True if so.
        """
        return datetime.datetime.today() <= self.deadline + self.created


class Student(Person):
    """Student."""

    def do_homework(self, todo: Homework, solution: str) -> Union[T, NoReturn]:
        """Homework.

        Returns Homework, if it's still in timeframe to do, either prints and
        returns None
        """
        if todo.is_active():
            return HomeworkResult(self, todo, solution)
        raise DeadlineError


class HomeworkResult:
    """Result.

    Class, that stores solution to given homework and author.
    """

    def __init__(self, author: Student, hw_name: Homework, solution: str):
        self.author = author
        self.solution = solution
        if not isinstance(hw_name, Homework):
            raise NotHomework
        self.hw_name = hw_name


class Teacher(Person):
    """Teacher."""

    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """Create hw.

        Creates new Homework.
        """
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls: Type[T], checking: HomeworkResult) -> bool:
        """Check.

        Checks given HomeworkResult, if solutions more or eq 5 returns True and
        also adds this Homework into homework_done dict
        """
        flag_sol_true = len(checking.solution) >= 5
        if flag_sol_true and checking not in cls.homework_done[checking.hw_name]:
            cls.homework_done[checking.hw_name].append(checking)
        return flag_sol_true

    @classmethod
    def reset_results(
        cls: Type[T], hw: Union[Homework, None] = None
    ) -> Optional[NoReturn]:
        """Reset.

        Deletes given Homework from homework_done dict Homework passed, if
        nothing passed clears entire homework_done dict
        """
        if hw is None:
            cls.homework_done.clear()
        else:
            del cls.homework_done[hw]


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
