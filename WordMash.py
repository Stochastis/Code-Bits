from cgitb import small
from operator import xor
import random as rnd
from secrets import choice


def WordMash(word0, word1):
    words = [word0, word1]
    smallerWordIndex = 0 if len(words[0]) <= len(words[1]) else 1
    wordLengthDifference = abs(len(words[0])-len(words[1]))

    offset = rnd.randint(0, wordLengthDifference)

    newWord = ''
    for i in range(1, offset+1):
        newWord += ' '
    newWord += words[smallerWordIndex]
    for i in range(1, len(words[smallerWordIndex ^ 1])-len(newWord)+1):
        newWord += ' '
    words[smallerWordIndex] = newWord

    for i in range(0, len(words[smallerWordIndex ^ 1])):
        if (rnd.randint(0, 1)):
            temp = words[0][i]
            words[0] = words[0][:i] + words[1][i] + words[0][i+1:]
            words[1] = words[1][:i] + temp + words[1][i+1:]

    print(words)


while True:
    input0 = input("Enter your first word.")
    input1 = input("Enter your second word.")
    WordMash(word0=input0, word1=input1)
    while True:
        userChoice = input(
            "Enter 1 for another mix with the same words. Enter 0 to try different words or exit.")
        if userChoice == '1':
            WordMash(word0=input0, word1=input1)
        elif userChoice == '0':
            while True:
                userChoice = input(
                    "Enter 1 for another mix with different words. Enter 0 to exit the program.")
                if userChoice == '1':
                    input0 = input("Enter your first word.")
                    input1 = input("Enter your second word.")
                    WordMash(word0=input0, word1=input1)
                    break
                elif userChoice == '0':
                    exit()
