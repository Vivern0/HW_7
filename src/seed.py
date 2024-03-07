from models import Student, Group, Lecturer, Subject, Mark
from connect_to_db import session
from random import randint, choice
from faker import Faker

NUMBER_OF_STUDENTS: int = randint(30, 50)
NUMBER_OF_GROUPS: int = 3
NUMBER_OF_LECTURERS: int = randint(3, 5)
NUMBER_OF_SUBJECTS: int = randint(5, 8)
MAX_NUMBER_OF_MARKS: int = 20


class FakeDataGenerator:
    def __init__(self, fake_gen: Faker) -> None:
        self.fake_gen = fake_gen

    def fake_student(self, groups_lst: list[Group]) -> Student:
        student = Student(
            full_name = self.fake_gen.name(),
            group = choice(groups_lst)
        )
        return student

    def fake_group(self) -> Group:
        return Group(group_name = self.fake_gen.word())

    def fake_lecturer(self) -> Lecturer:
        return Lecturer(full_name = self.fake_gen.name())

    def fake_subject(self, lecturer_lst: list[Lecturer]) -> Subject:
        subj = Subject(
            subject_name = self.fake_gen.word(),
            lecturer = choice(lecturer_lst)
        )
        return subj

    def fake_mark(
                self,
                student_inst: Student,
                subj_lst: list[Subject]
            ) -> Mark:
        mark = Mark(
            mark = randint(1, 100),
            date = self.fake_gen.date_this_year(),
            student = student_inst,
            subject = choice(subj_lst)
        )
        return mark

    def generate_fake_data(
                self,
                num_of_students: int,
                num_of_groups: int,
                num_of_lecturers: int,
                num_of_subjects: int,
                max_num_of_marks: int
            ) -> tuple:
        fake_groups = [
            self.fake_group() for _ in range(num_of_groups)
        ]

        fake_lecturers = [
            self.fake_lecturer() for _ in range(num_of_lecturers)
        ]

        fake_students = [
            self.fake_student(fake_groups)
            for _ in range(num_of_students)
        ]

        fake_subjects = [
            self.fake_subject(fake_lecturers)
            for _ in range(num_of_subjects)
        ]

        fake_marks = [
            self.fake_mark(stud, fake_subjects)
            for stud in fake_students
            for _ in range(1, randint(1, max_num_of_marks) + 1)
        ]

        return (
            fake_students, fake_groups, fake_lecturers, fake_subjects, fake_marks
        )


def insert_data(fake_data: list) -> None:
    for data in fake_data:
        session.add_all(data)
    session.commit()


def main() -> None:
    fake_data = FakeDataGenerator(Faker())

    fake_data = fake_data.generate_fake_data(
        NUMBER_OF_STUDENTS, NUMBER_OF_GROUPS, NUMBER_OF_LECTURERS,
        NUMBER_OF_SUBJECTS, MAX_NUMBER_OF_MARKS
    )

    insert_data(fake_data)


if __name__ == '__main__':
    main()