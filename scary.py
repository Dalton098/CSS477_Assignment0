import random

for i in range(10):
    s = "l"
    for j in range(100):
        lastChar = s[-1]
        prob = random.random()

        if (lastChar == 'l'):
            charToAdd = '_'

        elif (lastChar == '_'):
            if(prob >= 0 and prob < 0.5):
                charToAdd = 'a'
            elif(prob >= 0.5 and prob < 1):
                charToAdd = 'l'

        elif (lastChar == 'a'):
            if(prob >= 0 and prob < 0.4):
                charToAdd = 'm'
            elif(prob >= 0.4 and prob < 1):
                charToAdd = 'l'

        elif (lastChar == 'm'):
            if(prob >= 0 and prob < 0.8):
                charToAdd = '_'
            elif(prob >= 0.8 and prob < 1):
                charToAdd = '!'

        elif (lastChar == 'i'):
            if(prob >= 0 and prob < 0.95):
                charToAdd = 'v'
            elif(prob >= 0.95 and prob < 1):
                charToAdd = 'n'

        elif (lastChar == 'v'):
            chartoAdd = 'e'

        elif (lastChar == 'n'):
            chartoAdd = 'e'

        elif (lastChar == 'e'):
            chartoAdd = '!'

        elif (lastChar == '!'):
            if(prob >= 0 and prob < 0.7):
                charToAdd = '_'
            elif(prob >= 0.7 and prob < 0.9):
                charToAdd = 'l'
            elif(prob >= 0.9 and prob < 1):
                charToAdd = '!'

        s = s + charToAdd
    print(s)
