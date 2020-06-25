import random
names = input("What is your name? ")

def Greet(language, name):
    if language == "DE":
        print("Hello", names)
    else:
        print("Hallo", names)

Greet("DE", names) # Hello Zia
Greet("EN", names) # Hallo Zia

namess = ['Haris','Zia','Zorez','Yvonne','Rayan']
print(namess[random.randint(0, 4)])
