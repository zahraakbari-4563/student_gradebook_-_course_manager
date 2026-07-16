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
        print(f"Title: {self.title} - Score: {self.max_score}%")



