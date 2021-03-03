################################################################################
############################# Pig Latin Cipher #################################
################################################################################

# helper functions:

def convertToPL(message):
  normalMessage = message.lower()
  pigLatinMessage = ""
  if normalMessage[0] not in ('a', 'e', 'i', 'o', 'u'):
    pigLatinMessage = normalMessage[1:] + normalMessage[0]+ "ay"
  else:
    pigLatinMessage = normalMessage + "ay"
  return pigLatinMessage

def convertFromPL(message):
  pigLatinMessage = message
  normalMessage = ""
  normalMessage = pigLatinMessage[-3] + pigLatinMessage[:-3]
  return normalMessage

# main function

def runPigLatinConverter():
  print(" ")
  print("-------------------------------------------")
  print("|   Welcome to the Pig Latin Translator   |")
  print("-------------------------------------------")
  print(" ")
  message = input("Enter word to be converted into pig latin: ")
  newMessage = convertToPL(message)
  print(f"{message} becomes {newMessage}")
  

# runPigLatinConverter()