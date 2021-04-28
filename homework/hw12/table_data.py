"""Create data."""
from datetime import datetime, timedelta

from homework.hw12.base import session
from homework.hw12.table_create import Homework, HomeworkResult, Student, Teacher


session.query(Student).delete()
session.query(Teacher).delete()
session.query(Homework).delete()
session.query(HomeworkResult).delete()

student1 = Student(name="Stud_name", last_name="Std_lastname")
teacher1 = Teacher(name="Teacher_name", last_name="Tch_lastname")
homework1 = Homework(
    text="hardmode",
    teacher=teacher1,
    created=datetime.today(),
    deadline=datetime.now() + timedelta(1),
)
homework2 = teacher1.create_homework("asdf", 2)

homeworkresult2 = HomeworkResult(solution="ezpz", student=student1, homework=homework2)
homeworkresult1 = student1.do_homework(homework1, "asdffdsa")

teacher1.check_homework(homeworkresult1)
teacher1.check_homework(homeworkresult2)

session.add_all([student1, teacher1, homeworkresult1, homework1, homeworkresult2])

session.commit()
