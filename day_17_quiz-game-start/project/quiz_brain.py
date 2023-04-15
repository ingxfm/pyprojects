import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.current_question.quest)
        return f"Q.{self.question_number}: {question_text}"

    def correct_answer(self, answer_param):
        # here
        if self.question_list[self.question_number - 1].ans.lower() == answer_param.lower():
            self.score += 1
            print(f"That\'s right!")
            return True
        else:
            print("That\'s wrong!")
            return False
