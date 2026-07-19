class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        if score <= self.max_score:
            percentage = (score / self.max_score) * 100
            return round(percentage, 2)
        else:
            return "Invalid Score!"

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        print(f"Your grade is: {percentage}%")

    def display_info(self):
        print(f"Title: {self.title} - Score: {self.max_score}")

class Quiz(Assessment):
    def display_info(self):
        print(f"Quiz: {self.title} - Max_score: {self.max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 75:
            print("Great quiz result!")
        else:
            print("Needs more practice")


class Exam(Assessment):
    def display_info(self):
        print(f"Exam: {self.title} - Score: {self.max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if 100 >= percentage >= 55:
            print("Passed exam!")
        else:
            print("Failed exam!")


class Project(Assessment):
    def display_info(self):
        print(f"Project: {self.title} - Score: {self.max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)
        if percentage >= 80:
            print("Excellent project!")
        elif percentage >= 55:
            print("Project submitted!")
        else:
            print("Project needs improvement!")

