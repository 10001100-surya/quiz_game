class Quiz:
    def __init__(self ,  question_bank):
        self.question_no = 0
        self.question_bank = question_bank
        self.score = 0

    def still_has_question(self):
        if self.question_no < len(self.question_bank):
            return True
        else:
            return False

    def brain(self):
        current_question = self.question_bank[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q_no:{self.question_no}:{current_question.text}: Type True/False ?:").capitalize()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you got it right")
        else:
            print("wrong answer")
        print(f"correct answer is :{correct_answer}.")
        print(f"you score is :{self.score}/{self.question_no}\n")