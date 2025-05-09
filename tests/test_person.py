from students_db.db import Student


def test_student_constructor():
    test_student = Student(
        0,
        "Austin",
        "Long",
        "(555) 293-1982",
        "Forest Lake",
        "UNW",
        16,
        "Programming",
        "Freshman",
    )

    assert test_student.get_id() == 0
    assert test_student.get_first_name() == "Austin"
    assert test_student.get_last_name() == "Long"
    assert test_student.get_phone_number() == "(555) 293-1982"
    assert test_student.get_city() == "Forest Lake"
    assert test_student.get_school() == "UNW"
    assert test_student.get_age() == 16
    assert test_student.get_hobby() == "Programming"
    assert test_student.get_class_standing() == "Freshman"


def test_student_setters():
    test_student = Student(
        0,
        "Austin",
        "Long",
        "(555) 293-1982",
        "Forest Lake",
        "UNW",
        16,
        "Programming",
        "Freshman",
    )

    test_student.set_first_name("Logan")
    test_student.set_last_name("Holmstrom")
    test_student.set_phone_number("(320) 129-2983")
    test_student.set_city("St. Cloud")
    test_student.set_school("UNW")
    test_student.set_age(18)
    test_student.set_hobby("Exploring")
    test_student.set_class_standing("Freshman")

    assert test_student.get_id() == 0
    assert test_student.get_first_name() == "Logan"
    assert test_student.get_last_name() == "Holmstrom"
    assert test_student.get_phone_number() == "(320) 129-2983"
    assert test_student.get_city() == "St. Cloud"
    assert test_student.get_school() == "UNW"
    assert test_student.get_age() == 18
    assert test_student.get_hobby() == "Exploring"
    assert test_student.get_class_standing() == "Freshman"
