# Programmer: Austin Long
# Date: 2025-05-05
# Program: Students DB

# Import database. Make sure you run python from the root of the repository.
from db import StudentDatabase

# GUI code will go here eventually.

def main():
    with StudentDatabase("students.db") as student_db:
        pass

if __name__ == "__main__":
    main()
