"""Create tables."""
from collections import defaultdict
from datetime import datetime, timedelta
from typing import NoReturn, Optional, Type, Union

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from homework.hw12.base import Base, engine, session
from homework.hw6.task2_oop2 import DeadlineError, T


class Homework(Base):
    """Homework."""

    __tablename__ = "Homeworks"

    id = Column(Integer, primary_key=True)
    text = Column(String, unique=True)
    teacher_id = Column(Integer, ForeignKey("Teachers.id"))
    teacher = relationship("Teacher")
    created = Column(DateTime, default=datetime.now())
    deadline = Column(DateTime)

    def is_active(self) -> bool:
        """Active.

        Checks if this homework is still legitimate to do. True if so.
        """
        return datetime.today() <= self.deadline


class Student(Base):
    """Student."""

    __tablename__ = "Students"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    last_name = Column(String(50))

    def do_homework(self, todo: Homework, solution: str) -> Union[T, NoReturn]:
        """Homework.

        Returns Homework, if it's still in timeframe to do, either prints and
        returns None
        """
        if todo.is_active():
            h_res = HomeworkResult(solution=solution, student=self, homework=todo)
            session.add(h_res)
            session.commit()
            return h_res
        raise DeadlineError


class HomeworkResult(Base):
    """HomeworkResult."""

    __tablename__ = "HomeworkResults"

    id = Column(Integer, primary_key=True)
    solution = Column(String(50), unique=True)
    student_id = Column(Integer, ForeignKey("Students.id"))
    student = relationship("Student", foreign_keys=[student_id])
    homework_id = Column(Integer, ForeignKey("Homeworks.id"))
    homework = relationship("Homework", foreign_keys=[homework_id])
    completed = Column(Boolean)


class Teacher(Base):
    """Teacher."""

    __tablename__ = "Teachers"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    last_name = Column(String(50))

    """Teacher."""

    homework_done = defaultdict(list)

    def create_homework(self, text: str, deadline: int) -> Homework:
        """Create hw.

        Creates new Homework.
        """
        hw = Homework(
            text=text, deadline=datetime.now() + timedelta(deadline), teacher=self
        )
        session.add(hw)
        session.commit()
        return hw

    @classmethod
    def check_homework(cls: Type[T], checking: HomeworkResult) -> bool:
        """Check.

        Checks given HomeworkResult, if solutions more or eq 5 returns True and
        also adds this Homework into homework_done dict
        """
        checking.completed = len(checking.solution) >= 5
        session.commit()
        return checking.completed

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
    Base.metadata.create_all(engine)
