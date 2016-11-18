
def decrypt(encrypted_message):
    baseDecodedStr = "Your friend, Alice"
    baseEncodecodedStr = encrypted_message[encrypted_message.rfind('-')+1:]
    encryptionKey = getEncryptionKey(baseEncodecodedStr, baseDecodedStr,encrypted_message)
    print(encryptionKey)
    print(encrypted_message)
    return getDecryptedStr(encryptionKey, encrypted_message)


def getEncryptionKey(baseEncodecodedStr, baseDecodedStr,encrypted_message):
    encryptionKey = []
    for i in range(len(baseEncodecodedStr)):
        if 64 < ord(baseEncodecodedStr[i]) < 91 or 96 < ord(baseEncodecodedStr[i]) < 123:
            #what if the key is repeated? --> Currently do not consider this as option!
            #also key does not start at this position, then how do u do it?
            #What if key is longer than the given sequence?
            tempKey = ord(baseEncodecodedStr[i]) - ord(baseDecodedStr[i])
            if tempKey < 0:
                tempKey += 26
            encryptionKey.append(tempKey)
    #what the starting point of this key?
    #how can i determine key out of this? --> For time being i will continue to think that the key starts from start!!
    #found logic!!!!

    lengthOfKey = findNonRepeatingLength(encryptionKey)
    startingIndex = getStartingIndexOfKey(encrypted_message,lengthOfKey)

    return encryptionKey[startingIndex:startingIndex+lengthOfKey]

def getStartingIndexOfKey(encrypted_message,lengthOfKey):
    lenOfPrevStr = len(encrypted_message) - encrypted_message.rfind('-') + 1
    positionKey = 0
    cnt = 0
    for i in range(lenOfPrevStr):
        if 64 < ord(encrypted_message[i]) < 91 or 96 < ord(encrypted_message[i]) < 123:
            cnt += 1

    #issues might be here with the start of key index!!
    #test this carefully!
    positionKey = lengthOfKey - (cnt % lengthOfKey) + 1
    #print("positionKey : ", positionKey)
    return positionKey



def findNonRepeatingLength(encryptionKey):
    keyFinal = ''
    tempArr = list(map(str,encryptionKey))
    strKey = ''.join(tempArr)
    i = 0
    while strKey[:i+1] in strKey[i+1:] and i <len(strKey):
        i += 1
    #write your logic here!!
    return i

def getDecryptedStr(encryptionKey, encrypted_message):
    outputArr = []
    counter = -1
    for i in range(len(encrypted_message)):
        charNum = ord(encrypted_message[i])
        if 64 < charNum < 91 or 96 < charNum < 123:
            counter += 1
            keyItem = encryptionKey[counter % len(encryptionKey)]

            if 64 < charNum < 91 and charNum-keyItem < 65:
                tempChr = chr(91 - (65 - (charNum - keyItem)))
            elif 96 < charNum < 123 and charNum-keyItem < 97:
                tempChr = chr(123 - (97 - (charNum - keyItem)))
            else:
                tempChr = chr(charNum-keyItem)
            #print(keyItem, charNum, encrypted_message[i], tempChr)
            outputArr.append(tempChr)
        else:
            outputArr.append(encrypted_message[i])
    return ''.join(outputArr)

print(decrypt('elwepuqyez. -Atvt hrqgse, Cnikg'))