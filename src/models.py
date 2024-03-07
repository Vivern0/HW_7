from sqlalchemy import String, ForeignKey, CheckConstraint
from sqlalchemy.orm import declarative_base, Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.sql.sqltypes import DATE

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(100))
    group_fk: Mapped[int] = mapped_column(
        ForeignKey('groups.id', onupdate='CASCADE', ondelete='CASCADE')
    )
    group: Mapped['Group'] = relationship()


class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    group_name: Mapped[str] = mapped_column(String(100))


class Lecturer(Base):
    __tablename__ = 'lecturers'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(100))


class Subject(Base):
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    subject_name: Mapped[str] = mapped_column(String(100))
    lecturer_fk: Mapped[int] = mapped_column(
        ForeignKey('lecturers.id', onupdate='CASCADE', ondelete='CASCADE')
    )
    lecturer: Mapped['Lecturer'] = relationship()


class Mark(Base):
    __tablename__ = 'marks'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    mark: Mapped[int] = mapped_column(
        CheckConstraint('mark >= 0 AND mark <= 100')
    )
    date: Mapped[DATE] = mapped_column(DATE)
    student_fk: Mapped[int] = mapped_column(
        ForeignKey('students.id', onupdate='CASCADE', ondelete='CASCADE')
    )
    subject_fk: Mapped[int] = mapped_column(
        ForeignKey('subjects.id', onupdate='CASCADE', ondelete='CASCADE')
    )
    student: Mapped['Student'] = relationship()
    subject: Mapped['Subject'] = relationship()
