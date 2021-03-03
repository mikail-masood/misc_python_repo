#####################################################################################
################################   Cipher Library   #################################
#####################################################################################

import caesarCipher as caesar
import pigLatinCipher as pigLatin
import vigenereCipher as vigenere

def runCipherLibrary():
  # intro messages

  print('')
  print("---------------------------------------------")
  print("|       Welcome to The Cipher Library       |")
  print("---------------------------------------------")
  print('')
  print("Table of Contents: ")
  print(" 1. The Pig Latin Translator ")
  print(" 2. The Caesar Cipher Program")
  print(" 3. The Vigenere Cipher Program")
  print(" ")

  # exit loop confitions
  exitCipherLibrary = False
  exitPigLatin = False
  exitCaesarCipher = False
  exitVigenereCipher = False
  
  #Function Code
  while exitCipherLibrary == False:
    userChoice = input('Which program would you like to use (enter a number): ')
    if userChoice.lower() == "1":
      while exitPigLatin == False:
        pigLatin.runPigLatinConverter()
        continuePigLatin = input('Would you like to conitinue using this program? (y/n): ')
        if continuePigLatin.lower() == "n":
          exitPigLatin = True
        else:
          exitPigLatin = False
    elif userChoice.lower() == "2":
      while exitCaesarCipher == False:
        caesar.runCaesarCipherProgram()
        continueCaesarCipher = input('Would you like to conitinue using this program? (y/n): ')
        if continueCaesarCipher.lower() == 'n':
          exitCaesarCipher = True
        else:
          exitCaesarCipher = False
    elif userChoice.lower() == "3":
      while exitVigenereCipher == False:
        vigenere.runVigenereCipherProgram()
        continueVigenereCipher = input('Would you like to conitinue using this program? (y/n): ')
        if continueVigenereCipher.lower() == 'n':
          exitVigenereCipher = True
        else:
          exitVigenereCipher = False
    userNextChoice = input("Would you like to try another program? (y/n): ")
    if userNextChoice.lower() == 'n':
      exitCipherLibrary = True
    else:
      exitCipherLibrary = False
  
runCipherLibrary()