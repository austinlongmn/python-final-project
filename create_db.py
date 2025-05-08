import sqlite3


def main():
    with sqlite3.connect("students.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE Students (
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

        cursor.executescript("""
            INSERT INTO Students
                (first_name, last_name, phone_number, city, school, age, hobby, class_standing)
            VALUES
                ("Jamie", "Holmstrom", "(320) 248-9847", "St. Cloud", "SCSU", "51", "Fishing", "Alumni");


            INSERT INTO Students
                (first_name, last_name, phone_number, city, school, age, hobby, class_standing)
            VALUES
                ("Brayden", "Holmstrom", "(320) 784-2584", "St. Paul", "Bethel Uni.", "19", "History", "Junior");


            INSERT INTO Students
                (first_name, last_name, phone_number, city, school, age, hobby, class_standing)
            VALUES
                ("Jimmy", "Gotta", "(320) 249-3491", "St. Cloud", "SCSU", "37", "Teaching", "Alumni");


            INSERT INTO Students
                (first_name, last_name, phone_number, city, school, age, hobby, class_standing)
            VALUES
                ("Bob", "Goff", "(555) 352-5634", "Montgomery", "FSU", "22", "Travel", "Freshman");


            INSERT INTO Students
                (first_name, last_name, phone_number, city, school, age, hobby, class_standing)
            VALUES
                ("Breyon", "Gunn", "(555) 252-1252", "St. Paul", "UNWSP", "18", "Photography", "Senior");


            INSERT INTO Students
                (first_name, last_name, phone_number, city, school, age, hobby, class_standing)
            VALUES
                ("Anna", "Long", "(555) 292-9823", "Park Rapids", "UNWSP", "20", "Books", "Senior");


            INSERT INTO Students
                (first_name, last_name, phone_number, city, school, age, hobby, class_standing)
            VALUES
                ("Ann", "Sorenson", "(555) 239-2391", "Minneapolis", "UNWSP", "20", "Film", "Junior");


            INSERT INTO Students
                (first_name, last_name, phone_number, city, school, age, hobby, class_standing)
            VALUES
                ("Logan", "Holmstrom", "(320) 129-2983", "St. Cloud", "UNWSP", "18", "Exploring", "Freshman");


            INSERT INTO Students
                (first_name, last_name, phone_number, city, school, age, hobby, class_standing)
            VALUES
                ("Lexi", "Grzybowski", "(320) 120-2083", "St. Cloud", "SCTCC", "27", "Arts", "Alumni");


            INSERT INTO Students
                (first_name, last_name, phone_number, city, school, age, hobby, class_standing)
            VALUES
                ("Austin", "Long", "(555) 928-1982", "Forest Lake", "UNWSP", "16", "Programming", "Freshman");

        """)


        conn.commit()


if __name__ == "__main__":
    main()
