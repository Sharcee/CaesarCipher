import string

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

if __name__ == '__main__':
    key = prompt()
    print key
