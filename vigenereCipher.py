############################################################################
########################### The Vigenere Cipher ############################
############################################################################

##### helper functions #####

# choose what to do?
def chooseEncryptOrDecrypt():
  userOption = input("Do you want to encrypt or decrypt using the cipher? ")
  return userOption

# # Message to encrypt
def getMessage():
   stringToEncrypt = input("Enter message for encryption: ")
   return stringToEncrypt

# Message to decrypt
def getDecrypt():
    decryptMessage = input('Enter message for decryption: ')
    return decryptMessage

# Cipher Key
def getCipher():
  cipherKey = input('Enter the key: ')
  return cipherKey

# encryption
def vigenereEncryption(message, key):
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  translated = []
  keyIndex = 0
  key = key.upper()

  for char in message:
    num = alphabet.find(char.upper())
    if num != -1:
      num += alphabet.find(key[keyIndex])
      num %= len(alphabet)
      translated.append(alphabet[num])
      keyIndex += 1
      if keyIndex == len(key):
        keyIndex = 0
    else:
      translated.append(char)
  return ''.join(translated)

# decryption

def vigenereDecryption(message, key):
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  translated = []
  keyIndex = 0
  key = key.upper()

  for char in message:
    num = alphabet.find(char.upper())
    if num != -1:
      num -= alphabet.find(key[keyIndex])
      num %= len(alphabet)
      translated.append(alphabet[num])
      keyIndex += 1
      if keyIndex == len(key):
        keyIndex = 0
    else:
      translated.append(char)
  return ''.join(translated)  


# main fucntion

def runVigenereCipherProgram():
  print(" ")
  print("----------------------------------------------")
  print("|   Welcome to the Vigenere Cipher Program   |")
  print("----------------------------------------------")
  print(" ")
  exitLoop = False
  while exitLoop == False:
    option = chooseEncryptOrDecrypt()
    if option.lower() == "encrypt":
      myMessage = getMessage()
      cipherKey = getCipher()
      encryptedMessage = vigenereEncryption(myMessage, cipherKey)
      print(f'Encrypted Message: {encryptedMessage}')
      print(f'Decrypted Message: {myMessage.upper()}')
      exitLoop = True
    elif option.lower() == "decrypt":
      myMessage = getDecrypt()
      cipherKey = getCipher()
      decryptedMessage = vigenereDecryption(myMessage, cipherKey)
      print(f'Decrypted Message: {decryptedMessage}')
      print(f'Encrypted Message: {myMessage.upper()}')
      exitLoop = True
  

# runVigenereCipherProgram()