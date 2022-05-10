
import numpy as np
import re

# Remember to check for I/J


def groupin2s(sentence):
    i = 0
    grouped = []
    while(i < len(sentence)-1):
        grouped.append(sentence[i]+sentence[i+1])
        i += 2
    return grouped


def encrypt(myList):
    sentenceTemp = re.sub(
        r'[^a-zA-Z]', '', input("Enter plain input> ").lower())
    if(len(sentenceTemp) <= 0):
        return
    sentence = ''
    for i in range(len(sentenceTemp)-1):
        sentence += sentenceTemp[i]
        if(i % 2 == 0 and sentenceTemp[i+1] == sentenceTemp[i]):
            sentence += 'x'
    sentence += sentenceTemp[len(sentenceTemp)-1]
    if(len(sentence) % 2 == 1):
        sentence += 'x'

    cipher = ''
    sentence = groupin2s(sentence)
    for grouped in sentence:
        firstLetter = grouped[0].upper() if grouped[0].upper() != 'J' else 'I'
        secondLetter = grouped[1].upper() if grouped[1].upper() != 'J' else 'I'
        firstIndex = [-1, -1]
        secondIndex = [-1, -1]
        # check if in the same row
        isfound = False
        for row in myList:
            if(firstLetter in row and secondLetter in row):
                # shift them right
                isfound = True
                cipher += row[row.index(firstLetter) +
                              1 if row.index(firstLetter)+1 < len(row) else 0]
                cipher += row[row.index(secondLetter) +
                              1 if row.index(secondLetter)+1 < len(row) else 0]
            elif(firstLetter in row or secondLetter in row):
                if firstLetter in row:
                    firstIndex = [myList.index(row), row.index(
                        firstLetter)]
                elif secondLetter in row:
                    secondIndex = [myList.index(row), row.index(
                        secondLetter)]

        if(not isfound):
            # check if in the same column
            if(firstIndex[1] == secondIndex[1]):
                cipher += myList[firstIndex[0] +
                                 1 if firstIndex[0] < 4 else 0][firstIndex[1]]
                cipher += myList[secondIndex[0] +
                                 1 if secondIndex[0] < 4 else 0][secondIndex[1]]
            # for angle switching
            else:
                cipher += myList[firstIndex[0]][secondIndex[1]]
                cipher += myList[secondIndex[0]][firstIndex[1]]
    print(sentence)
    print('Cipher output:', cipher)


def decrypt(myList):
    sentenceTemp = re.sub(
        r'[^a-zA-Z]', '', input("Enter Cipher input> ").lower())
    if(len(sentenceTemp) <= 0):
        return
    sentence = sentenceTemp

    cipher = ''
    i = 0
    while(i < len(sentence)-1):
        firstLetter = sentence[i].upper()
        secondLetter = sentence[i+1].upper()
        firstIndex = [-1, -1]
        secondIndex = [-1, -1]
        # check if in the same row
        isfound = False
        for row in myList:
            if(firstLetter in row and secondLetter in row):
                # shift them right
                isfound = True
                cipher += row[row.index(firstLetter) -
                              1 if row.index(firstLetter) > 0 else 4]
                cipher += row[row.index(secondLetter) -
                              1 if row.index(secondLetter) > 0 else 4]
            elif(firstLetter in row or secondLetter in row):
                if firstLetter in row:
                    firstIndex = [myList.index(row), row.index(
                        firstLetter)]
                elif secondLetter in row:
                    secondIndex = [myList.index(row), row.index(
                        secondLetter)]

        if(not isfound):
            # check if in the same column
            if(firstIndex[1] == secondIndex[1]):
                cipher += myList[firstIndex[0] -
                                 1 if firstIndex[0] > 0 else 4][firstIndex[1]]
                cipher += myList[secondIndex[0] -
                                 1 if secondIndex[0] > 0 else 4][secondIndex[1]]
            # for angle switching
            else:
                cipher += myList[firstIndex[0]][secondIndex[1]]
                cipher += myList[secondIndex[0]][firstIndex[1]]
        i += 2

    print('Plaintext output:', cipher)


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
key = list(dict.fromkeys(list(input("Please enter your key > ").upper())))

myList = key
myList.extend(list(filter(lambda letter: key.count(letter) == 0, letters)))
myList = np.array(myList).reshape(5, 5)
print('Playfair application will use the following key matrix')
for row in myList:
    for letter in row:
        print(letter+", ", end="")
    print('')
myList = np.ndarray.tolist(myList)
while(True):
    choice = input('Please choose operation (1) Encrypt   (2) De-crypt > ')
    if(choice == '1'):
        encrypt(myList)
    elif(choice == '2'):
        decrypt(myList)
    else:
        print('Invalid choice')
        break
