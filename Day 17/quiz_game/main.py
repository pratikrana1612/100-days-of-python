from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    qu = Question(question["question"], question["correct_answer"])
    question_bank.append(qu)

# for question in question_bank:
#         print(question.text)
#         print(question.answer)


quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question()

print(f"Your Final Score is {quiz_brain.score}/{quiz_brain.question_number}")