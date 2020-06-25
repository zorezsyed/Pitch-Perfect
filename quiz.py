import random 
import cups

symbols = ['+','-']
TOTAL = 5

def sendToPrint(file_name):
    conn = cups.Connection ()
    printers = conn.getPrinters ()
    printer_name = printers.keys()[6]
    conn.printFile (printer_name, file_name, "Fact Test Report", {})
    print ("Sent to printer:",printer_name)

class Question:
    def __init__(self, first, second,symbol):
        self.first = first
        self.second = second
        self.symbol = symbol

    def getKey(self):
        if self.symbol == 0: #Addition 
            return self.first+self.second
        else:
            return self.first+self.second
    
    def addUserAnswer(self,answer):
        self.useranswer=answer

    def getUserAnswer(self):
        return self.useranswer

    def printQuestion(self):
        if self.symbol:
            return (str(self.first) + " + " + str(self.second) + " = " + str(self.getKey()))
        else:
            return (str(self.first) + " - " + str(self.second) + " = " + str(self.getKey()))

    def check_answer_input(self,answer_input):
        if self.symbol == 0: #Addition 
            if self.first+self.second == answer_input:
                return True
            else:
                return False
        else: #Substraction
            if self.first-self.second == answer_input:
                return True
            else:
                return False
        
qu = []        
def createQuestion():
    first = random.randint(0, 9)
    symbol = random.randint(0, 1)
    second = random.randint(0, 9)
    q= Question(first,second,symbol)
    return q

count = 0

for i in range(0,TOTAL): 
    q = createQuestion()

    question = str(q.first) + " " + symbols[q.symbol] + " " + str(q.second) +" = "    
    print ("Please enter your answers below:")    
    answer_input = int(input(question))
    q.addUserAnswer(answer_input)
    qu.append(q)
    result = q.check_answer_input(answer_input) 

    if result == True:
        print ("Correct")
        count = count+1
    else:
        print ("Incorrect")


f = open("test_result.txt", "w")
f.write("\n\n")
f.write("Face Sheet Result\n")



print ("Correct answers: "+str(count))
percent = (float(count)/float(TOTAL)) * 100
print("Your score: " + str(percent) + "%")

f.write("Your score: " + str(percent) + "%\n")
for i in range(len(qu)):
    print(str(i+1) + ") " + qu[i].printQuestion() + " You entered " + str(qu[i].getUserAnswer()) + " " + str(qu[i].check_answer_input(qu[i].getUserAnswer())))
    f.write(str(i+1) + ") " + qu[i].printQuestion() + " You entered " + str(qu[i].getUserAnswer()) + " " + str(qu[i].check_answer_input(qu[i].getUserAnswer()))+ "\n")

f.close()
sendToPrint("test_result.txt")
