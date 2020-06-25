import random
randomName = []
names = ["John","Jack","Jason","James","Jake","Jacob"]
rel = ["grandfather","grandson","father","greatgrandfather","greatgrandson"]
class Syed:
    def __init__(self, name, relative):
        self.name = name
        self.relative = relative
    
    def printName(self):
        print (self.name + " is the " + rel[self.relative])

for i in range(1,10):
    h = Syed(names[random.randint(0,len(names)-1)],random.randint(0,len(rel)-1))
    randomName.append(h)
for i in randomName:
    i.printName()
