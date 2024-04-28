from question_model import Question
from data import question_data
from quiz_brain import Quizbrain


question_bank=[]
for question in question_data:
    question_bank.append(Question(question["text"],question["answer"]))

ques=Quizbrain(question_bank)

ques.next_question()

while ques.still_have_questions():
    ques.next_question()

print(f"Your final score is: {ques.score}")
