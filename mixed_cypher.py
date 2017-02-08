import string
from string import maketrans

def findCypher(word):
    '''
    Takes in a key and extracts the unique characters. Then, it will append the
    remaining characters of the alphabet and return a string of characters. This
    is the cypher key
    '''
    word = word.lower() + string.lowercase
    cypher = ""
    for i in range(len(word)):
        if word[i] not in cypher:
            cypher = cypher + word[i]
    return cypher

def prompt():
    key = raw_input("Please enter a keyword for the mixed cipher: ")
    return key

def encrypt(msg, cypher):
    cypher = cypher + cypher.upper()
    alphabet = string.letters
    translation = maketrans(alphabet, cypher)
    return msg.translate(translation)

if __name__ == '__main__':
    key = prompt()
    # print(key)

    print("Plaintext: " + string.ascii_lowercase )
    cypher = findCypher(key)
    print("Ciphertext: " + cypher )

    message = raw_input("Please enter a message you would like to encrypt: ")

    encoded = encrypt(message, cypher)
    print encoded
