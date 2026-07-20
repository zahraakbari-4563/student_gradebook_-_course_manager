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
        if student_id in self.students and course_code in self.courses:
            self.students[student_id].enroll_course(course_code)
            self.courses[course_code].add_student(student_id)
        else:
            print("Student or course not found.")


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
        percentages = []
        for assessment in self.courses[course_code].assessments:
            score = self.grades[student_id][course_code][assessment.title]
            percentage = assessment.calculate_percentage(score)
            percentages.append(percentage)
        average = sum(percentages) / len(percentages)
        return average

    def show_report(self, student_id):
        student = self.students[student_id]
        print(f"Name: {student.name}")
        if student_id not in self.grades:
            print("No grades recorded for this student.")
            return
        for course in student.courses:
            print(f"\nCourse: {course}")
            if course in self.grades[student_id]:
                for assessment_title, score in self.grades[student_id][course].items():
                    print(f"{assessment_title}: {score}")
                    for assessment_obj in self.courses[course].assessments:
                        if assessment_obj.title == assessment_title:
                            assessment_obj.grade_message(score)
                            print("=" * 3)
                            break
                average = self.calculate_average(student_id, course)
                print(f"Average: {average: .2f}")
                print(f"letter Grade: {self.get_letter_grade(average)}")
                print(f"Result: {self.get_result(average)}")

    def get_letter_grade(self, average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        elif average >= self.passing_grade:
            return "E"
        else:
            return "F"

    def search_student(self, keyword):
        for student in self.students.values():
            if keyword == student.get_id() or keyword.lower() == student.name.lower():
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

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students.values():
            student.display_info()
            print("-" * 30)


    def show_dashboard(self):
        print("\n==== Dashboard ====")
        print(f"Total Students: {len(self.students)}")
        print(f"Total Courses: {len(self.courses)}")
        total_assessments = 0
        for course in self.courses.values():
            total_assessments += len(course.assessments)
        print(f"Total Assessments: {total_assessments}")

        total_grades = 0
        for student_grades in self.grades.values():
            for course_grade in student_grades.values():
                total_grades += len(course_grade)
        print(f"Total Grades Recorded: {total_grades}")


    @staticmethod
    def show_menu():
        print("\n===== Student Gradebook Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Add Course")
        print("4. Enroll Student in Course")
        print("5. Add Assignment")
        print("6. Record Grade")
        print("7. View Student Report")
        print("8. Search Student")
        print("9. Delete Student")
        print("10.Dashboard")
        print("0. Exit")
        print("====" * 10)