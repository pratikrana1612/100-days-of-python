

class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list=question_list
        self.score=0

    def still_has_question(self):
        return self.question_number<=len(self.question_list)-1

    def next_question(self):
        question=self.question_list[self.question_number]
        useranswer=input(f"Q.{self.question_number+1}: {question.text} (True/False)?:")
        self.check_answer(useranswer,question.answer)
        self.question_number+=1

    def check_answer(self,useranswer,correctanswer):
        if(useranswer.lower()==correctanswer.lower()):
            print("Yes You got it")
            self.score+=1
        else:
            print("That's Wrong")
        print(f"The correct answer was: {correctanswer}.")
        print(f"The current score is:{self.score}/{self.question_number+1}")
        print("\n")
