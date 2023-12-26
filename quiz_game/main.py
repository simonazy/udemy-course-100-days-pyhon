from data import question_data 
from question_model import Question
from quiz_brain import QuizBrain

q_list = []
for item in question_data:
    q = Question(item['question'], item['correct_answer'])
    q_list.append(q) 

qb = QuizBrain(q_list) 

while qb.still_has_question():
    qb.next_question()


print("You've completed the quiz")
print(f"Your final score was: {qb.score}/{qb.question_number}")





