class Student:
    def __init__(self, student_id, name, email):
        self.__student_id = student_id
        self.name = name
        self.__email = email
        self.courses = []


    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if "@gmail.com" in email:
            self.__email = email
        else:
            print("Email not valid")

    def enroll_course(self, course_code):
        self.courses.append(course_code)

    def display_info(self):
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.__email}")
        print(f"Courses: {self.courses}")


