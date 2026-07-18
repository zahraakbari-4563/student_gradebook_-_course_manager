class GradeBook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = 55


    def add_student(self, student):
        self.students[student.get_id()] = student

    def add_course(self, course):
        self.courses[course.course_code] = course


    def enroll_student(self, student_id, course_code):
        if course_code in self.courses and student_id in self.students:
            self.courses[course_code].enroll_student(student_id)
        else:
            print("Course or student not found!")


    def add_assessment(self, course_code, assessment):
        if course_code in self.courses:
            self.courses[course_code].add_assessment(assessment)
        else:
            print("Course not found.")