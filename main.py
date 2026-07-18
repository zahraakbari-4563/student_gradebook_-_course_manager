from data import gradebook
from student import Student
from course import Course
from assessment import Quiz, Exam, Project

while True:
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
    print("0. Exit")
    print("====" * 10)
    choice = input("Choose an option: ")
    if choice == "1":
        student_id = input("Student ID: ")
        name = input("Name: ")
        email = input("Email: ")
        student = Student(student_id, name, email)
        gradebook.add_student(student)
        print("Student Added.")

    elif choice == "2":
        gradebook.view_students()

    elif choice == "3":
        code = input("Course Code: ")
        name = input("Course Name: ")
        course = Course(code, name)
        gradebook.add_course(course)
        print("Course Added.")

    elif choice == "4":
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        gradebook.enroll_student(student_id, course_code)
        print("Student Enrolled.")

    elif choice == "5":
        course_code = input("Course Code: ")
        title = input("Assessment Title: ")
        max_score = int(input("Max Score: "))
        assessment_type = input("Type (quiz/exam/project): ").lower()

        if assessment_type == "quiz":
            assessment = Quiz(title, max_score)
        elif assessment_type == "exam":
            assessment = Exam(title, max_score)
        else:
            assessment = Project(title, max_score)
        gradebook.add_assessment(course_code, assessment)
        print("Assessment Added.")

    elif choice == "6":
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        assessment = input("Assessment Title: ")
        score = float(input("Score: "))
        gradebook.record_grade(student_id, course_code, assessment, score)

    elif choice == "7":
        student_id = input("Student ID: ")
        gradebook.show_report(student_id)

    elif choice == "8":
        keyword = input("Enter Student ID or Name: ")
        student = gradebook.search_student(keyword)
        if student:
            student.display_info()
        else:
            print("Student not found.")

    elif choice == "9":
        student_id = input("Student ID: ")
        gradebook.delete_student(student_id)
        print("Student Deleted.")

    elif choice == "0":
        break