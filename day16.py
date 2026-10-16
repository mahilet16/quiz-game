
#quiz game true or false
from data import question_data

class Question:
    def __init__(self, question, answer):
        self.text = question
        self.answer = answer
question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_answer= question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
class QuizBrain:
    def __init__(self,question_list):
        self.question_number =0
        self.score=0
        self.question_list =question_list


    def next_question(self):
            current_question = self.question_list[self.question_number]
            self.question_number+=1
            user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False)").lower()
            self.cheek_answer(user_answer,current_question.answer)
    def still_has_questions(self):
        return self.question_number<len(self.question_list)

    def cheek_answer(self,user_answer,correct_answer):
        if user_answer==correct_answer.lower():
            print("You got it right! ")
            self.score+=1
        else:
            print("that is wrong! ")
        print(f"the correct answer is {correct_answer}")
        print(f"Your current score is:{self.score}/{self.question_number}")
        print("\n")

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("YOu've completed the quiz")
print(f"Your final score is:{quiz.score}/{quiz.question_number}")




