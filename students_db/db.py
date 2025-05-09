# Database code will go here.

import sqlite3
from student import Student


class StudentDatabase:
    def __init__(self, database_file: str, reset_database: bool = True) -> None:
        self.__connection = sqlite3.connect(database_file)
        self.__cursor = self.__connection.cursor()

        if reset_database:
            self.__cursor.execute(
                """
                DROP TABLE IF EXISTS Students;
            """
            )

        self.__ensure_table()

        if reset_database:
            with open("students_db/test_data.sql") as test_data_file:
                self.__cursor.executescript(test_data_file.read())

    def __ensure_table(self):
        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Students (
                id INTEGER PRIMARY KEY NOT NULL,
                first_name TEXT,
                last_name TEXT,
                phone_number TEXT,
                city TEXT,
                school TEXT,
                age INTEGER,
                hobby TEXT,
                class_standing TEXT
            );
        """
        )

    def commit(self):
        self.__connection.commit()

    def close(self):
        self.__connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == None and exc_value == None and traceback == None:
            self.commit()
        self.close()
