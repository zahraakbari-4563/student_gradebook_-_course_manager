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


    def record_grade(self, student_id, course_code, assessment_title, score):

        if student_id not in self.students:
            print("Student not found!")
            return
        if course_code not in self.courses:
            print("Course not found!")
            return
        if student_id not in self.grades:
            self.grades[student_id] = {}
        if course_code not in self.grades[student_id]:
            self.grades[student_id][course_code] = {}

        self.grades[student_id][course_code][assessment_title] = score

    def calculate_average(self,student_id, course_code):
        grades = self.grades[student_id][course_code].values()
        average = sum(grades) / len(grades)
        return average

    def show_report(self, student_id):
        student = self.students[student_id]
        print(f"Student ID: {student.student_id}")
        print(f"Name: {student.name}")
        print(F"Courses: {student.courses}")
        if student_id not in self.grades:
            print("No grades recorded for this student.")
            return
        for course in student.courses:
            print(f"\nCourse: {course}")
            if course in self.grades[student_id]:
                for assessment, score in self.grades[student_id][course].items():
                    print(f"{assessment}: {score}")
                average = self.calculate_average(student_id, course)
                print(f"Average: {average: .2f}")
                print(f"Result: {self.get_result(average)}")

    def search_student(self, keyword):
        for student in self.students.values():
            if keyword == student.student_id or keyword.lower() == student.name.lower():
                return student
        return None


    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]

        else:
            print("Student not found.")


    def get_result(self, average):
       if average>= self.passing_grade:
           return "Passed"
       else:
           return "Failed"