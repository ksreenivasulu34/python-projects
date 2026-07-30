class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.question_list = q_list
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer_input = input(f"Q.{self.question_number}: {current_question.question}. 'True/False?': ")
        print(answer_input)
        if(answer_input == current_question.answer):
            print("You got it right!")
            self.correct_answers += 1
        else:
            print("You are wrong!")
        print(f"The correct answer was: { current_question.answer }")
        print(f"Your current score is: { self.correct_answers } / {self.question_number}")
