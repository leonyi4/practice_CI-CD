import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents, Person

@pytest.fixture
def empty_classroom():
    teacher = Teacher("Professor Snape")
    return Classroom(teacher, [], "Potions")

def test_add_student(empty_classroom):
    student = Student("Harry Potter")
    empty_classroom.add_student(student)
    assert len(empty_classroom.students) == 1

    with pytest.raises(TooManyStudents):
        for i in range(10):
            empty_classroom.add_student(Student(f"Student_{i}"))

def test_remove_student(empty_classroom):
    student1 = Student("Hermione Granger")
    student2 = Student("Ron Weasley")

    empty_classroom.add_student(student1)
    empty_classroom.add_student(student2)

    empty_classroom.remove_student("Hermione Granger")
    assert len(empty_classroom.students) == 1
    assert student1 not in empty_classroom.students

def test_add_too_many_students(empty_classroom):
    for i in range(10):
        student = Student(f"Student_{i}")
        empty_classroom.add_student(student)

    with pytest.raises(TooManyStudents):
        extra_student = Student("ExtraStudent")
        empty_classroom.add_student(extra_student)

    # Ensure that the number of students remains at the maximum allowed (10)
    assert len(empty_classroom.students) == 10


def test_change_teacher(empty_classroom):
    new_teacher = Teacher("Professor McGonagall")
    empty_classroom.change_teacher(new_teacher)
    assert empty_classroom.teacher == new_teacher

def test_change_teacher_with_invalid_teacher(empty_classroom):
    new_teacher = "InvalidTeacher"
    empty_classroom.change_teacher(new_teacher)
    assert empty_classroom.teacher == new_teacher


def test_person_creation():
    person = Person("Albus Dumbledore")
    assert person.name == "Albus Dumbledore"

def test_teacher_inherits_from_person():
    teacher = Teacher("Professor Flitwick")
    assert isinstance(teacher, Person)

def test_student_inherits_from_person():
    student = Student("Luna Lovegood")
    assert isinstance(student, Person)
