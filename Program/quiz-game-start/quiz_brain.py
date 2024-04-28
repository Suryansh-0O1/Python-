class Quizbrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        ques=input(f"Q.{self.question_number + 1}. {self.question_list[self.question_number].text} (True/False)\n")
        self.check(ques)
        self.question_number+=1

    def still_have_questions(self):
        return self.question_number < len(self.question_list)
            
    def check(self,ques):
        if self.question_list[self.question_number].answer == ques:
            self.score+=1
            print("Correct")
        else:
            print("Incorrect")