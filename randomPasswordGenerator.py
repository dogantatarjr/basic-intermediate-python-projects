import random


def listToString(s):
    str1 = ""

    for ele in s:
        str1 += ele

    return str1

upperLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

fullList = []

for i in range(0, len(upperLetters)):
    fullList.append(upperLetters[i])

for i in range(0, len(lowerLetters)):
    fullList.append(lowerLetters[i])

for i in range(0, len(symbols)):
    fullList.append(symbols[i])

for i in range(0, len(numbers)):
    fullList.append(numbers[i])

passw = []

for i in range(0, 15):
    passw.append(random.choice(fullList))

print("Random Password:", listToString(passw))