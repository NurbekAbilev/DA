__author__ = 'Nurbek Abilev'

import json as jsonlib
import difflib

def printMeanings(arr):
    for meaning in arr:
        print(meaning)

def levenshteinDistance(s1,s2):
    cost = 0
    if(len(s2)>=5):
        return 1000
    len1 = len(s1)
    len2 = len(s2)

    if (len1 == 0):
      return len2
    if (len2 == 0):
      return len1

    if (s1[-1] == s2[-1]):
        cost = 0
    else:
        cost = 1

    return min(
        levenshteinDistance(s1[:-1],s2)+1,
        levenshteinDistance(s1,s2[:-1])+1,
        levenshteinDistance(s1[:-1],s2[:-1])+cost,
    )

def getClosest(target,words):
    dist = 1000
    key = None
    p = 0
    for word in words:
        temp = levenshteinDistance(target,word)
        print(word + " " + str(temp))
        print(p/len(words)*100)
        p+=1
        if(temp<dist):
            dist = temp
            key = word
            # input("DEBUG:"+key)
    
    print(key)
    return key

# 0 for difflib
# 1 to use custom function
MODE = 1

with open("data.json","r") as file:
    data = jsonlib.load(file)

    while True:
        cutoff = 0.8
        exitcode = 'exit'
        inputString = input("Enter word(type '"+exitcode+"' to exit):")
        if(inputString==exitcode):
            break

        if(inputString in data):
            printMeanings(data[inputString])

        else:
            closestMatch = ""

            if(MODE==0):
                closeMatches = difflib.get_close_matches(inputString,data,1,cutoff)
                closestMatch = closeMatches[0]
            if(MODE==1):
                closestMatch = getClosest(inputString,data)

            if closestMatch:
                answer = input("Did you mean '"+closestMatch+"' instead? Enter Y if yes, or N if no:")
                if(answer=="Y" or answer=="y"):
                    printMeanings(data[closestMatch])
                else:
                    otherVariants = difflib.get_close_matches(inputString,data,10,cutoff-0.3)
                    print("Other varaints:")
                    print(otherVariants)
            else:
                print("No words found in dictionary!!!")






