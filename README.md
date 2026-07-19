# Student Gradebook & Course manager
Description of the project.

## Full Name
Zahra Akbari

## Project Title
Student Gradebook & Course Manager

## Project Description
This project is a console-based Python application for managing students, courses, assessments, and grades. It allows users to add students and courses, enroll students, record grades, calculate averages, display letter grades, and generate student reports.

## Features
- Add, view, search, update, and delete new students.
- View all students
- Enroll students in courses
- Add assessments (Quiz, Exam, Project)
- Record student grades
- Calculate average grade and show pass/fail result.
- Display letter grades (A–F)
- Generate student reports

## How to Run
1. Clone or download the project.
2. Open the project folder in PyCharm.
3. Run `main.py`.
4. Use the menu to manage students, courses, and grades.

## Classes
- Student
- Course
- Assessment
- Quiz(child class)
- Exam(child class)
- Project(child class)
- GradeBook

## OOP Concepts Used

### Encapsulation
The `Student` class uses private attributes with getters and setters to protect student information.

### Inheritance
`Quiz`, `Exam`, and `Project` inherit from the `Assessment` class.

### Method Overriding
The `display_info()` and `grade_message()` methods are overridden in the child classes to provide different behavior for quizzes, exams, and projects.

## Input Validation
- Checks menu choices.
- Validates student IDs and student emails.
- Prevents grades below 0 or above the maximum score.
- Displays error messages instead of crashing.

## Custom Features
1. Dashboard-Displays statistics such as total students, courses, assessments, and recorded grades. 
2. Letter Grades-Automatic letter grade calculation (A–F) based on the student's average.