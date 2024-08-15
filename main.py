from generalknowledge import question_data
from questionmodel import Question
from quizbrain import Quiz

question_bank = []
for question in question_data:
    questions = question["text"]
    answers = question["answer"]
    new_question = Question(text=questions, answer=answers)
    question_bank.append(new_question)

user_1 = Quiz(question_bank)
while user_1.still_has_question():
    user_1.brain()

print(f"your total score is {user_1.score}/{user_1.question_no}.")


