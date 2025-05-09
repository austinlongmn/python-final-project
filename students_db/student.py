# SQL Schema:
# CREATE TABLE Students (
#     id INTEGER PRIMARY KEY NOT NULL,
#     first_name TEXT,
#     last_name TEXT,
#     phone_number TEXT,
#     city TEXT,
#     school TEXT,
#     age INTEGER,
#     hobby TEXT,
#     class_standing TEXT
# );


class Student:
    """Represents a student in the database."""

    def __init__(
        self,
        id: int,
        first_name: str,
        last_name: str,
        phone_number: str,
        city: str,
        school: str,
        age: int,
        hobby: str,
        class_standing: str,
    ) -> None:
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._city = city
        self._school = school
        self._age = age
        self._hobby = hobby
        self._class_standing = class_standing

    def get_id(self) -> int:
        """Gets the id of the row in the database"""
        return self._id

    def get_first_name(self) -> str:
        """Gets the first name of the student."""
        return self._first_name

    def set_first_name(self, value) -> None:
        self._first_name = value

    def get_last_name(self) -> str:
        """Gets the last name of the student."""
        return self._last_name

    def set_last_name(self, value) -> None:
        self._last_name = value

    def get_phone_number(self) -> str:
        """Gets the student's phone number."""
        return self._phone_number

    def set_phone_number(self, value) -> None:
        self._phone_number = value

    def get_city(self) -> str:
        """Gets the city were the student lives in."""
        return self._city

    def set_city(self, value) -> None:
        self._city = value

    def get_school(self) -> str:
        """Gets the school the student attend(s/ed)."""
        return self._school

    def set_school(self, value) -> None:
        self._school = value

    def get_age(self) -> int:
        """Gets the student's age."""
        return self._age

    def set_age(self, value) -> None:
        self._age = value

    def get_hobby(self) -> str:
        """Gets one of the student's primary hobbies."""
        return self._hobby

    def set_hobby(self, value) -> None:
        self._hobby = value

    def get_class_standing(self) -> str:
        """Gets the class standing of the student. (Freshman, Sophomore, etc.)"""
        return self._class_standing

    def set_class_standing(self, value) -> None:
        self._class_standing = value
