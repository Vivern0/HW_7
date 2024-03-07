from models import Student, Group, Lecturer, Subject, Mark
from connect_to_db import session
from sqlalchemy import func, desc, and_


def select_1():
    res = session.query(
        Student.full_name,
        func.round(func.avg(Mark.mark), 2).label('avg_mark')
    ).select_from(Student).join(Mark, Mark.student_fk == Student.id)\
    .group_by(Student.id).order_by(desc('avg_mark')).limit(5).all()

    return res


def select_2():
    res = session.query(
        Student.full_name,
        func.round(func.avg(Mark.mark), 2).label('avg_mark')
    ).select_from(Student).join(Mark, Mark.student_fk == Student.id)\
    .join(Subject, Subject.id == Mark.subject_fk)\
    .where(Subject.subject_name == 'learn').group_by(Student.id)\
    .order_by(desc('avg_mark')).limit(1).all()

    return res


def select_3():
    res = session.query(
        Group.group_name,
        func.round(func.avg(Mark.mark), 2).label('avg_mark')
    ).select_from(Group).join(Student, Student.group_fk == Group.id)\
    .join(Mark, Mark.student_fk == Student.id)\
    .join(Subject, Subject.id == Mark.subject_fk)\
    .where(Subject.subject_name == 'for').group_by(Group.id).all()
    
    return res


def select_4():
    res = session.query(
        func.round(func.avg(Mark.mark), 2).label('avg_mark')
    ).select_from(Mark).all()

    return res


def select_5():
    res = session.query(
        Subject.subject_name.label('subjects')
    ).select_from(Lecturer).join(Subject, Subject.lecturer_fk == Lecturer.id)\
    .where(Lecturer.full_name == 'Joanne Lee').all()

    return res


def select_6():
    res = session.query(
        Student.full_name
    ).select_from(Student).where(Student.group_fk == '3').all()

    return res


def select_7():
    res = session.query(
        Student.full_name,
        Mark.mark
    ).select_from(Student).join(Mark, Mark.student_fk == Student.id)\
    .join(Subject, Subject.id == Mark.subject_fk)\
    .where(and_(Student.group_fk == '2', Subject.subject_name == 'use')).all()

    return res


def select_8():
    res = session.query(
        Lecturer.full_name.label('lecturer_name'),
        func.round(func.avg(Mark.mark), 2).label('avg_mark')
    ).select_from(Lecturer).join(Subject, Subject.lecturer_fk == Lecturer.id)\
    .join(Mark, Mark.subject_fk == Subject.id)\
    .group_by(Lecturer.id).all()

    return res


def select_9():
    res = session.query(
        Subject.subject_name.distinct()
    ).select_from(Student).join(Mark, Mark.student_fk == Student.id)\
    .join(Subject, Subject.id == Mark.subject_fk)\
    .where(Student.full_name == 'Ryan Cox').all()

    return res


def select_10():
    res = session.query(
        Subject.subject_name.distinct()
    ).select_from(Student).join(Mark, Mark.student_fk == Student.id)\
    .join(Subject, Subject.id == Mark.subject_fk)\
    .join(Lecturer, Lecturer.id == Subject.lecturer_fk)\
    .where(and_(
        Lecturer.full_name == 'Joanne Lee', Student.full_name == 'John Tate'
    )).all()

    return res


def select_11():
    res = session.query(
        func.round(func.avg(Mark.mark), 2).label('avg_mark')
    ).select_from(Student).join(Mark, Mark.student_fk == Student.id)\
    .join(Subject, Subject.id == Mark.subject_fk)\
    .join(Lecturer, Lecturer.id == Subject.lecturer_fk)\
    .where(and_(
        Lecturer.full_name == 'Joanne Lee', Student.full_name == 'John Tate'
    )).all()

    return res


def select_12():
    subq = session.query(
        func.max(Mark.date)
    ).select_from(Mark).where(Mark.subject_fk == Subject.id)\
    .scalar()

    res = session.query(
        Student.full_name,
        Mark.mark
    ).select_from(Student).join(Mark, Mark.student_fk == Student.id)\
    .join(Subject, Subject.id == Mark.subject_fk)\
    .join(Group, Group.id == Student.group_fk)\
    .where(and_(
        Subject.subject_name == 'claim', 
        Group.group_name == 'century',
        Mark.date == subq
    )).all()

    return res


if __name__ == '__main__':
    print('------------ Select 1 ------------')
    print(select_1())

    print('------------ Select 2 ------------')
    print(select_2())

    print('------------ Select 3 ------------')
    print(select_3())

    print('------------ Select 4 ------------')
    print(select_4())

    print('------------ Select 5 ------------')
    print(select_5())

    print('------------ Select 6 ------------')
    print(select_6())

    print('------------ Select 7 ------------')
    print(select_7())

    print('------------ Select 8 ------------')
    print(select_8())

    print('------------ Select 9 ------------')
    print(select_9())

    print('------------ Select 10 ------------')
    print(select_10())

    print('------------ Select 11 ------------')
    print(select_11())

    print('------------ Select 12 ------------')
    print(select_12())
