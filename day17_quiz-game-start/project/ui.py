# built-ins
from tkinter import *

# My own
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 10, "italic")
WHITE = "#dfe6e9"


class QuizUI:

    def __init__(self, quiz_brain_attr: QuizBrain):
        self.quiz = quiz_brain_attr
        self.timing_bg = None

        # window
        self.window = Tk()
        self.window.title("Quizkaton")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # label
        self.score_label = Label(text=f"Score: {self.quiz.score}",
                                 font=SCORE_FONT,
                                 bg=THEME_COLOR,
                                 fg="white"
                                 )

        self.score_label.grid(column=1, row=0)

        # canvas
        self.canvas = Canvas(width=300, height=250, bg="white")

        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="question text",
                                                     fill=THEME_COLOR,
                                                     font=FONT,
                                                     width=280,
                                                     )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # buttons
        true_answer_image = PhotoImage(file="images/true.png")
        self.answer_true_button = Button(image=true_answer_image,
                                         command=self.check_mark_true_button,
                                         highlightthickness=0)
        self.answer_true_button.grid(column=0, row=2)
        false_answer_image = PhotoImage(file="images/false.png")
        self.answer_false_button = Button(image=false_answer_image,
                                          command=self.cross_mark_false_button,
                                          highlightthickness=0)
        self.answer_false_button.grid(column=1, row=2)

        # new question text
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have reached the end of the quiz.\n\n"
                                        f"Your score is {self.quiz.score}.")
            self.answer_true_button.config(state="disabled")
            self.answer_false_button.config(state="disabled")

    def check_mark_true_button(self):
        is_correct_answer = self.quiz.correct_answer("True")
        self.feedback_to_player(is_correct_answer)

    def cross_mark_false_button(self):
        is_correct_answer = self.quiz.correct_answer("False")
        self.feedback_to_player(is_correct_answer)

    def feedback_to_player(self, is_correct_answer):
        if is_correct_answer:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
