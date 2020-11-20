import time

def ceaserCipher(inputString, shiftKey):
    
    #inputString = inputString.lower()

    getCipheredLol = ""

    for i in inputString:
        letter = ord(i) + shiftKey
        #if letter > ord("z"):
        #    letter = letter - 26
        cipheredLetter = chr(letter)
        getCipheredLol = getCipheredLol + cipheredLetter

    print(getCipheredLol)

print("Choose a word or sentence to put through a Ceaser Cipher: ")
inputString = input()
print("You have chosen string '", inputString, "'.")
print()
print()
time.sleep(1)

print("Now choose the number of places (as an integer) that you would like to shft the key: ")
shiftKey = int(input())
print("You have chosen value '", shiftKey, "'.")
print()
print()
time.sleep(1)


ceaserCipher(inputString, shiftKey)
