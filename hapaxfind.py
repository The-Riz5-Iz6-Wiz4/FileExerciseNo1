#import string
import string

#Function to find a word used only once per work/file
#Thing of note for this function, it can remove punctuation, but cannot remove "
#therefore the txt files must not have " for it to be accurate. I assume this also applies to '.

def hapaxfind(filepath):

    file = open(filepath, encoding="utf8")
    word = file.read()
    loWord = word.lower()
    cleanWord = loWord.translate(str.maketrans('', '', string.punctuation)) #removes all punctuation except quotation marks
    wordList = cleanWord.split()

    #using dict to assign every unique word as a key and value to determine its frequency in any text
    myDict ={key: 0 for key in wordList}
    for words in wordList:
        myDict[words] += 1
    #if the frequency is one then it is a hapax and gets printed
    for words in myDict:
        if myDict[words] == 1:
            print(words)


hapaxfind()
#on windows the string should be input as r'desired filepath here'. unsure if needed for mac.