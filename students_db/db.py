# Database code will go here.

import sqlite3


class StudentsDatabase:
    pass


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
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone_number = phone_number
        self.__city = city
        self.__school = school
        self.__age = age
        self.__hobby = hobby
        self.__class_standing = class_standing

    def get_id(self) -> int:
        """Gets the id of the row in the database"""
        return self.__id

    def get_first_name(self) -> str:
        """Gets the first name of the student."""
        return self.__first_name

    def set_first_name(self, value) -> None:
        self.__first_name = value

    def get_last_name(self) -> str:
        """Gets the last name of the student."""
        return self.__last_name

    def set_last_name(self, value) -> None:
        self.__last_name = value

    def get_phone_number(self) -> str:
        """Gets the student's phone number."""
        return self.__phone_number

    def set_phone_number(self, value) -> None:
        self.__phone_number = value

    def get_city(self) -> str:
        """Gets the city were the student lives in."""
        return self.__city

    def set_city(self, value) -> None:
        self.__city = value

    def get_school(self) -> str:
        """Gets the school the student attend(s/ed)."""
        return self.__school

    def set_school(self, value) -> None:
        self.__school = value

    def get_age(self) -> int:
        """Gets the student's age."""
        return self.__age

    def set_age(self, value) -> None:
        self.__age = value

    def get_hobby(self) -> str:
        """Gets one of the student's primary hobbies."""
        return self.__hobby

    def set_hobby(self, value) -> None:
        self.__hobby = value

    def get_class_standing(self) -> str:
        """Gets the class standing of the student. (Freshman, Sophomore, etc.)"""
        return self.__class_standing

    def set_class_standing(self, value) -> None:
        self.__class_standing = value
