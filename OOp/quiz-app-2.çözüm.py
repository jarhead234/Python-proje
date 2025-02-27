# Quiz sınıfı
#   - questions     => soru listesi
#   - questionIndex => gösterilecek soru

# quiz = Quiz(questions)
# quiz.getQuestion()     => soru 1, soru 2... (nesne)
# quiz.displayQuestion()




import random

class question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        if answer not in self.choices:
            raise ValueError("hatalı bilgi")
        return self.answer == answer

class quiz:
    def __init__(self,questions):
        self.questions = random.sample(questions,len(questions))
        self.questionIndex = 0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()

        print(f"soru {self.questionIndex + 1}: {question.text}") 

        for q in question.choices:
            print("-" + q)









q1 = question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
q2 = question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
q3 = question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")

sorular = [q1,q2,q3]

quiz = quiz(sorular)

print(quiz.displayQuestion())


