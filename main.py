from connection.connection import ConnectionDB

class Student:
    # def __init__(self, student_id, first_name, last_name, national_code, age, gender):
    #     self.id = student_id
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.national_code = national_code
    #     self.age = age
    #     self.gender = gender

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
                "gender" VARCHAR(255) NOT NULL);""")
            ConnectionDB.close_db()
            print("Table created successfully")
        except Exception as e:
            print("ERROR",e)

    @staticmethod
    def alter_table():
        try:
            ConnectionDB.execute_query("""ALTER TABLE
            "students" ADD PRIMARY KEY("student_id");""")
            ConnectionDB.close_db()
            print("Table altered successfully")
        except Exception as e:
            print("ERROR", e)

class Course:
    # def __init__(self, course_id, course_name, course_description):
    #     self.id = course_id
    #     self.course_name = course_name
    #     self.course_description = course_description

    @staticmethod
    def create_table():
        try:
            ConnectionDB.execute_query(
                """CREATE TABLE "courses"(
            "course_id" SERIAL NOT NULL,
            "course_name" VARCHAR(255) NOT NULL,
            "course_hours" TIME(0) WITHOUT TIME ZONE NOT NULL,
            "student_id" SERIAL NOT NULL
        );""")
            ConnectionDB.close_db()
            print("Table created successfully")
        except Exception as e:
            print("ERROR", e)

    @staticmethod
    def alter_table():
        try:
            ConnectionDB.execute_query("""ALTER TABLE
            "courses" ADD PRIMARY KEY("course_id");""")
            ConnectionDB.close_db()
            print("Table altered successfully")
        except Exception as e:
            print("ERROR", e)

class Grades:
    # def __init__(self, grade_id, student_id, course_id, grade_achieved):
    #     self.id = grade_id
    #     self.student_id = student_id
    #     self.course_id = course_id
    #     self.grade_achieved = grade_achieved

    @staticmethod
    def create_table():
        try:
            ConnectionDB.execute_query(
                """CREATE TABLE "grades"(
                "grade_id" SERIAL NOT NULL,
                "student_id" SERIAL NOT NULL,
                "course_id" SERIAL NOT NULL,
                "grade_achieved" FLOAT(53) NOT NULL
                );""")
            ConnectionDB.close_db()
            print("Table created successfully")
        except Exception as e:
            print("ERROR",e)

    @staticmethod
    def alter_table():
        try:
            ConnectionDB.execute_query("""ALTER TABLE
            "grades" ADD PRIMARY KEY("grade_id");
            ALTER TABLE
            "grades" ADD CONSTRAINT "grades_course_id_unique" UNIQUE("course_id");""")
            ConnectionDB.close_db()
            print("Table altered successfully")
        except Exception as e:
            print("ERROR", e)
class Enrollment:
    # def __init__(self, enrollment_id, student_id, address, date):
    #     self.id = enrollment_id
    #     self.student_id = student_id
    #     self.address = address
    #     self.date = date

    @staticmethod
    def create_table():
        try:
            ConnectionDB.execute_query(
                """CREATE TABLE "enrollments"(
            "enrollment_id" SERIAL NOT NULL,
            "student_id" SERIAL NOT NULL,
            "address" TEXT NOT NULL,
            "date" DATE NOT NULL
            );""")
            ConnectionDB.close_db()
            print("Table created successfully")
        except Exception as e:
            print("ERROR",e)

    @staticmethod
    def alter_table():
        try:
            ConnectionDB.execute_query("""ALTER TABLE
            "enrollments" ADD PRIMARY KEY("enrollment_id");
            ALTER TABLE
            "enrollments" ADD CONSTRAINT "enrollments_student_id_unique" UNIQUE("student_id");""")
            ConnectionDB.close_db()
            print("Table altered successfully")
        except Exception as e:
            print("ERROR", e)


class StCo:
    # def __init__(self, enrollment_id, student_id, address, date):
    #     self.id = enrollment_id
    #     self.student_id = student_id
    #     self.address = address
    #     self.date = date

    @staticmethod
    def create_table():
        try:
            ConnectionDB.execute_query(
                """CREATE TABLE "st-co"(
            "student_id" SERIAL NOT NULL,
            "course_id" SERIAL NOT NULL
                );""")
            ConnectionDB.close_db()
            print("Table created successfully")
        except Exception as e:
            print("ERROR",e)

"""
ALTER TABLE
    "st-co" ADD CONSTRAINT "st_co_course_id_foreign" FOREIGN KEY("course_id") REFERENCES "courses"("course_id");
ALTER TABLE
    "st-co" ADD CONSTRAINT "st_co_student_id_foreign" FOREIGN KEY("student_id") REFERENCES "students"("student_id");
ALTER TABLE
    "enrollments" ADD CONSTRAINT "enrollments_student_id_foreign" FOREIGN KEY("student_id") REFERENCES "students"("student_id");
ALTER TABLE
    "grades" ADD CONSTRAINT "grades_course_id_foreign" FOREIGN KEY("course_id") REFERENCES "courses"("course_id");"""
