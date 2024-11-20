from connection import ConnectionDB
from tabulate import tabulate


class Student:

    @staticmethod
    def create_table():
        try:
            ConnectionDB.execute_query(
                """CREATE TABLE "students"(
                "student_id" SERIAL NOT NULL,
                "first_name" VARCHAR(255) NOT NULL,
                "last_name" VARCHAR(255) NOT NULL,
                "code_meli" INTEGER NOT NULL,
                "age" INTEGER NOT NULL,
                "gender" VARCHAR(255) NOT NULL);""").close()
            print("Table created successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def alter_table():
        try:
            ConnectionDB.execute_query("""ALTER TABLE
            "students" ADD PRIMARY KEY("student_id");""").close()
            print("Table altered successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def insert_data():
        try:
            ConnectionDB.execute_query("""INSERT INTO students (first_name, last_name, code_meli, age, gender) VALUES
            ('John', 'Doe', 123456789, 20, 'Male'),
            ('Jane', 'Smith', 987654321, 22, 'Female'),
            ('Ali', 'Rezaei', 456123789, 21, 'Male'),
            ('Sara', 'Moradi', 789321654, 23, 'Female');""").close()
            print("Data inserted successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def __show_data_table():
        try:
            return ConnectionDB.execute_query("""SELECT * FROM students;""").fetchall()
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def delete_table():
        try:
            ConnectionDB.execute_query("""DROP TABLE students;""").close()
            print("Table deleted successfully")
        except Exception as e:
            print("ERROR", e)

    @classmethod
    def display(cls):
        items = cls.__show_data_table()
        headers = ["student_id", "first_name", "last_name", "code_meli", "age", "gender"]
        print(tabulate(items, headers=headers, tablefmt="grid"))


class Course:

    @staticmethod
    def create_table():
        try:
            ConnectionDB.execute_query(
                """CREATE TABLE "courses"(
            "course_id" SERIAL NOT NULL,
            "course_name" VARCHAR(255) NOT NULL,
            "course_hours" TIME(0) WITHOUT TIME ZONE NOT NULL,
            "student_id" SERIAL NOT NULL
        );""").close()
            print("Table created successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def alter_table():
        try:
            ConnectionDB.execute_query("""ALTER TABLE
            "courses" ADD PRIMARY KEY("course_id");""").close()
            print("Table altered successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def insert_data():
        try:
            ConnectionDB.execute_query("""INSERT INTO courses (course_name, course_hours, student_id) VALUES
            ('Mathematics', '01:30:00', 1),
            ('Physics', '02:00:00', 2),
            ('Computer Science', '03:00:00', 3),
            ('Chemistry', '02:30:00', 4);""").close()
            print("Data inserted successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def __show_data_table():
        try:
            return ConnectionDB.execute_query("""SELECT * FROM courses;""").fetchall()
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def delete_table():
        try:
            ConnectionDB.execute_query("""DROP TABLE courses;""").close()
            print("Table deleted successfully")
        except Exception as e:
            print("ERROR", e)

    @classmethod
    def display(cls):
        items = cls.__show_data_table()
        headers = ["course_id", "course_name", "courses_hours", "student_id"]
        print(tabulate(items, headers=headers, tablefmt="grid"))


class Grades:

    @staticmethod
    def create_table():
        try:
            ConnectionDB.execute_query(
                """CREATE TABLE "grades"(
                "grade_id" SERIAL NOT NULL,
                "student_id" SERIAL NOT NULL,
                "course_id" SERIAL NOT NULL,
                "grade_achieved" FLOAT(53) NOT NULL
                );""").close()
            print("Table created successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def alter_table():
        try:
            ConnectionDB.execute_query("""ALTER TABLE
            "grades" ADD PRIMARY KEY("grade_id");
            ALTER TABLE
            "grades" ADD CONSTRAINT "grades_course_id_unique" UNIQUE("course_id");""").close()
            print("Table altered successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def insert_data():
        try:
            ConnectionDB.execute_query("""INSERT INTO grades (student_id, course_id, grade_achieved) VALUES
            (1, 1, 88.5),
            (2, 2, 92.0),
            (3, 3, 78.3),
            (4, 4, 85.0);""").close()
            print("Data inserted successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def __show_data_table():
        try:
            return ConnectionDB.execute_query("""SELECT * FROM grades;""").fetchall()

        except Exception as e:
            print("ERROR", e)

    @classmethod
    def display(cls):
        items = cls.__show_data_table()
        headers = ["grade_id", "student_id", "course_id", "grade_achieved"]
        print(tabulate(items, headers=headers, tablefmt="grid"))

    @staticmethod
    def delete_table():
        try:
            ConnectionDB.execute_query("""DROP TABLE grades;""").close()
            print("Table deleted successfully")
        except Exception as e:
            print("ERROR", e)


class Enrollment:
    @staticmethod
    def create_table():
        try:
            ConnectionDB.execute_query(
                """CREATE TABLE "enrollments"(
            "enrollment_id" SERIAL NOT NULL,
            "student_id" SERIAL NOT NULL,
            "address" TEXT NOT NULL,
            "date" DATE NOT NULL
            );""").close()
            print("Table created successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def insert_data():
        try:
            ConnectionDB.execute_query("""INSERT INTO enrollments (student_id, address, date) VALUES
            (1, '123 Elm Street, CityA', '2024-09-01'),
            (2, '456 Oak Avenue, CityB', '2024-09-02'),
            (3, '789 Pine Road, CityC', '2024-09-03'),
            (4, '321 Maple Lane, CityD', '2024-09-04');""").close()
            print("Data inserted successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def alter_table():
        try:
            ConnectionDB.execute_query("""ALTER TABLE
            "enrollments" ADD PRIMARY KEY("enrollment_id");
            ALTER TABLE
            "enrollments" ADD CONSTRAINT "enrollments_student_id_unique" UNIQUE("student_id");""").close()
            print("Table altered successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def __show_data_table():
        try:
            return ConnectionDB.execute_query("""SELECT * FROM enrollments;""").fetchall()
        except Exception as e:
            print("ERROR", e)

    @classmethod
    def display(cls):
        items = cls.__show_data_table()
        headers = ["enrollments_id", "student_id", "address", "date"]
        print(tabulate(items, headers=headers, tablefmt="grid"))

    @staticmethod
    def delete_table():
        try:
            ConnectionDB.execute_query("""DROP TABLE enrollments;""").close()
            print("Table deleted successfully")
        except Exception as e:
            print("ERROR", e)


class StCo:
    @staticmethod
    def create_table():
        try:
            ConnectionDB.execute_query(
                """CREATE TABLE "st-co"(
            "student_id" SERIAL NOT NULL,
            "course_id" SERIAL NOT NULL
                );""").close()
            print("Table created successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def insert_data():
        try:
            ConnectionDB.execute_query("""INSERT INTO "st-co" (student_id, course_id) VALUES
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4);""").close()
            print("Data inserted successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def __show_data_table():
        try:
            return ConnectionDB.execute_query("""SELECT * FROM st-co;""").fetchall()
        except Exception as e:
            print("ERROR", e)

    @classmethod
    def display(cls):
        items = cls.__show_data_table()
        headers = ["student_id", "course_id"]
        print(tabulate(items, headers=headers, tablefmt="grid"))

    @staticmethod
    def delete_table():
        try:
            ConnectionDB.execute_query("""DROP TABLE st-co;""").close()
            print("Table deleted successfully")
        except Exception as e:
            print("ERROR", e)


"""
ALTER TABLE
    "st-co" ADD CONSTRAINT "st_co_course_id_foreign" FOREIGN KEY("course_id") REFERENCES "courses"("course_id");
ALTER TABLE
    "st-co" ADD CONSTRAINT "st_co_student_id_foreign" FOREIGN KEY("student_id") REFERENCES "students"("student_id");
ALTER TABLE
    "enrollments" ADD CONSTRAINT "enrollments_student_id_foreign" FOREIGN KEY("student_id") REFERENCES "students"("student_id");
ALTER TABLE
    "grades" ADD CONSTRAINT "grades_course_id_foreign" FOREIGN KEY("course_id") REFERENCES "courses"("course_id");
"""

obj1 = Student()
obj1.display()
