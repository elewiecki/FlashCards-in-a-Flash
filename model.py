'''
model to process input.txt, write to output.txt

what it needs:

- function to read from input.txt and convert to term def dict
    - use regex to identify term def pairs, event date pairs, etc.
    - after finding patterns, identify additional important terms using frequencies, these create new keys with empty string values
    --> dictionary <String : String>
- function to take in dictionary returned from previous function and write to output.txt in quizlet import format
    - format should be 
            term + ',' + def + '\n'
        for each key:value pair

'''



def createCardDictionary():
    toRet = {}
    
    #first pass
    def findPatterns():
        # does not return anything, modifies toRet
    def findKeywords():
        # does not return anything, modifies toRet
    
    return toRet



def writeOutput(cardDict):
    #does not return anything, overwrites output.txt

