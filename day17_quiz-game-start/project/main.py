from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUI

question_list = []
for item in range(len(question_data)):
    new_q = Question(question_data[item]['question'], question_data[item]['correct_answer'])
    question_list.append(new_q)

quiz = QuizBrain(question_list)
# let's pass the quiz to the quiz UI.
quiz_ui = QuizUI(quiz)

print(f"You completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}.")
