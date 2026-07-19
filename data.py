from gradebook import GradeBook
from student import Student
from course import Course
from assessment import Quiz, Exam, Project

gradebook = GradeBook()
student_1 = Student("S001", "Ahmad Rahimi", "ahmad@gmail.com" )
student_2 = Student("S002", "Fatima Mohammadi", "fatima@gmail.com")
student_3 = Student("S003", "Ali Karimi", "ali@gmail.com")
student_4 = Student("S004", "Sara Ahmadi", "sara@gmail.com")


course_1 = Course("PY101", "Python Programming")
course_2 = Course("WD101", "Web Development")


quiz_1 = Quiz("Quiz 1", 10)
exam_1 = Exam("Midterm Exam", 100)
project_1 = Project("Final Project", 100)


gradebook.add_student(student_1)
gradebook.add_student(student_2)
gradebook.add_student(student_3)
gradebook.add_student(student_4)

gradebook.add_course(course_1)
gradebook.add_course(course_2)


gradebook.enroll_student("S001", "PY101")
gradebook.enroll_student("S002", "PY101")
gradebook.enroll_student("S003", "WD101")
gradebook.enroll_student("S004", "WD101")

gradebook.add_assessment("PY101", quiz_1)
gradebook.add_assessment("PY101", exam_1)
gradebook.add_assessment("PY101", project_1)
gradebook.add_assessment("WD101", quiz_1)
gradebook.add_assessment("WD101", exam_1)
gradebook.add_assessment("WD101", project_1)

gradebook.record_grade("S001", "PY101", "Quiz 1", 8)
gradebook.record_grade("S001", "PY101", "Midterm Exam", 75)
gradebook.record_grade("S001", "PY101", "Final Project", 90)