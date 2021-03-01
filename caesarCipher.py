############################################################################
########################### Caesar Cipher Program ##########################
############################################################################

## Helper functions ##

# Double Alphabet
def getDoubleAlphabet(alphabet):
   doubleAlphabet = alphabet + alphabet
   return doubleAlphabet

# Ask user to encrypt or decrypt a message

def chooseEncryptOrDecrypt():
    userOption = input("Do you want to encrypt or decrypt? ")
    return userOption

# Message to encrypt
def getMessage():
   stringToEncrypt = input("Please enter a message to encrypt: ")
   return stringToEncrypt

# Message to decrypt
def getDecrypt():
    decryptMessage = input('Enter message for decryption: ')
    return decryptMessage

# Cipher Key
def getCipherKey():
   shiftAmount = input( "Please enter a key (whole number from 1-25): ")
   return shiftAmount

# Encrypt Message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + (-1*int(cipherKey))
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

#Decrypt message
def decryptMessage2(message, cipherKey, alphabet):
    decryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for char in uppercaseMessage:
        pos = alphabet.find(char)
        newPos = pos + int(cipherKey)
        if char in alphabet:
            decryptedMessage = decryptedMessage + alphabet[newPos]
        else:
            decryptedMessage = decryptedMessage + char
    return decryptedMessage


## End of Helper Functions ##

# Main Function to be run
# run this to encrypt/decrpt

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    option = chooseEncryptOrDecrypt()
    if option.lower() == "encrypt":
        myMessage = getMessage()
    elif option.lower() == "decrypt":
        myMessage = getDecrypt()
    myCipherKey = getCipherKey()
    if option.lower() == "encrypt":
        myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
        print(f'Encrypted Message: {myEncryptedMessage}')
        myDecryptedMessage = decryptMessage2(myEncryptedMessage, myCipherKey, myAlphabet2)
        print(f'Decypted Message: {myDecryptedMessage}')
    else:
        myDecryptedMessage = decryptMessage2(myMessage, myCipherKey, myAlphabet2)
        print(f'Decrypted Message: {myDecryptedMessage}')
        myEncryptedMessage = encryptMessage(myDecryptedMessage, myCipherKey, myAlphabet2)
        print(f'Encypted Message: {myEncryptedMessage}')

runCaesarCipherProgram()