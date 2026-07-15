class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []
        self.assessments = []

    def add_student(self, student_id):
        self.students.append(student_id)

    def add_assessment(self, assessment):
        self.assessments.append(assessment)

    def find_assessment(self, title):
        for assessment in self.assessments:
            if assessment.title == title:
                return assessment
            else:
                print("Assessment not found")
        return None

    def display_info(self):
        print(f"Course Code: {self.course_code} " )
        print(f"Course Name: {self.course_name}")
        print(f"Students: {self.students}")
        print(f"Assessments:")
        for assessment in self.assessments:
            assessment.display_info()


