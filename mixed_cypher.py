import string
from string import maketrans

def findCypher(word):
    '''
    Takes in a key and extracts the unique characters. Then, it will append the
    remaining characters of the alphabet and return a string of characters. This
    is the cypher key
    '''
    word = word + string.lowercase
    cypher = ""
    for i in range(len(word)):
        if word[i] not in cypher:
            cypher = cypher + word[i]
    return cypher

def prompt():
    key = raw_input("Please enter a keyword for the mixed cipher: ")
    return key

def encrypt(msg, cypher):
    alphabet = string.lowercase
    translation = maketrans(alphabet, cypher)
    return msg.translate(translation)

if __name__ == '__main__':
    key = prompt()
    print(key)

    cypher = findCypher(key)
    print cypher

    message = raw_input("Please enter a message you would like to encrypt: ")

    encoded = encrypt(message, cypher)
    print encoded
