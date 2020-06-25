import random

TOTAL = 100
randomName = []

names = ["Zia", "Zorez","Haris","Yvonne","Rayan","Nachtigall"]
class Syed:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printName(self):
        print (self.name + " is " + str(self.age) + " years old")

for i in range (1,TOTAL):
    r = Syed(names[random.randint(0,len(names)-1)],random.randint(0,1000))
    randomName.append(r)

# for i in randomName:
#     i.printName()

class Question:
    def __init__(self, first, second,symbol):
        self.first = first
        self.second = second
        self.symbol = symbol

    def getKey(self):
        if self.symbol == 0: #Addition 
            return self.first+self.second
    
    def addUserAnswer(self,answer):
        self.useranswer=answer

    def getUserAnswer(self):
        return self.useranswer

    def printQuestion(self):
        if self.symbol:
            print str(self.first) + " + " + str(self.second) + " = " + str(self.getKey())
        else:
            print str(self.first) + " - " + str(self.second) + " = " + str(self.getKey())

q1 = Question(5,3,0)
q1.addUserAnswer(10)
print q1.getKey()
print q1.getUserAnswer()
print q1.printQuestion()

