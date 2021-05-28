introString=input("enter your introduction:")
characterCount=0
wordsCount=1
for i in introString:
    characterCount=characterCount+1
    if(i ==' '):
        wordsCount=wordsCount+1
print("number of words in the strings:")
print(wordsCount) 
print("number of characters in the strings:")
print(characterCount)      