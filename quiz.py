import random 

symbols = ['+','-']
TOTAL = 3

def check_answer_input(f, s, sym, in_answer):
    if sym == 0: #Addition 
        if f+s == in_answer:
            return True
        else:
            return False
    else: #Substraction
        if f-s == in_answer:
            return True
        else:
            return False
        
def createQuestion():
    first = random.randint(0, 9)
    symbol = random.randint(0, 1)
    second = random.randint(0, 9)
    return first, second, symbol
count = 0
for i in range(0,TOTAL): 
    first, second, symbol = createQuestion()
    question = str(first) + " " + symbols[symbol] + " " + str(second) +" = "    
    print ("Please enter your answers below:")    
    answer_input = int(input(question))
    result = check_answer_input(first, second, symbol, answer_input)  
    if result == True:
        print "Correct"
        count = count+1
    else:
        print "Incorrect"

print ("Correct answers: "+str(count))
percent = (float(count)/float(TOTAL)) * 100
print("Your score: " + str(percent) + "%")

    
   


