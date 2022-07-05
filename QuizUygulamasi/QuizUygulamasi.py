#sorulari, kullanici cevaplarini ve dogu cevaplari alir
class Question:
    def __init__(self, test, choices, answer):
        self.text = test
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer


class Quiz:
    def __init__(self,question):
        self.questions = question
        self.score = 0 
        self.questionIndex = 0 

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):  #ilkili indexteki soruyu ekrana basma islemi yapar
        question = self.getQuestion()
        print(f" Soru { self.questionIndex + 1 } :  { question.text }   ")
        for q in question.choices:
            print("-"+ q)

        answer = input("Cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
        
        
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()


    def showScore(self):
        print("score: ", self.score)


    def displayProgress(self):
        totalQuestion = len(self.questions) 
        questionNumbers = self.questionIndex + 1

        if questionNumbers > totalQuestion : 
            print("Quiz Bitti.")
        else:
            print(f" Question { questionNumbers } of { totalQuestion } ".center(100,'*'))




#sorular
q1 = Question("en iyi programlama dili hangisidir? ", ["C#" , "python", "javascript", "java" ], "python")
q2 = Question("en popular programlama dili hangisidir? ", ["C#" , "python", "javascript", "java" ], "python")
q3 = Question("en cok kazandiran programlama dili hangisidir? ", ["C#" , "python", "javascript", "java" ], "python")
q4 = Question("en cok sevilen programlama dili hangisidir? ", ["C#" , "python", "javascript", "java" ], "python")
q5 = Question("en kolay programlama dili hangisidir? ", ["C#" , "python", "javascript", "java" ], "python")
questions = [q1,q2,q3,q4,q5]    #sorularin tutuldugu dizi

#programin calismaya basladigi yer
quiz = Quiz(questions)
quiz.loadQuestion()
