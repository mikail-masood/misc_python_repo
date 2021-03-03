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
  if pigLatinMessage[-3] not in ('a', 'e', 'i', 'o', 'u'):
    normalMessage = pigLatinMessage[:-2]
  else:
    normalMessage = pigLatinMessage[-3] + pigLatinMessage[:-3]
  return normalMessage

# main function

def runPigLatinConverter():
  print(" ")
  print("-------------------------------------------")
  print("|   Welcome to the Pig Latin Translator   |")
  print("-------------------------------------------")
  print(" ")
  option = input("Do you want to encrypt or decrypt pig latin? (enter encrypt or decrypt) ")
  if option.lower() == "encrypt":
    message = input("Enter word to be converted into pig latin: ")
    newMessage = convertToPL(message)
    print(f"{message} becomes {newMessage}")
  elif option.lower() == "decrypt":
    message = input("Enter word to be converted from pig latin: ")
    newMessage = convertFromPL(message)
    print(f"{message} becomes {newMessage}")
  else:
    print('error try again')


# runPigLatinConverter()