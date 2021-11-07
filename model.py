# 
# model to process input.txt, write to output.txt

# what it needs:

# - function to read from input.txt and convert to term def dict
#     - use regex to identify term def pairs, event date pairs, etc.
#     - after finding patterns, identify additional important terms using frequencies, these create new keys with empty string values
#     --> dictionary <String : String>
# - function to take in dictionary returned from previous function and write to output.txt in quizlet import format
#     - format should be 
#             term + ',' + def + '\n'
#         for each key:value pair

# 


import re



def createCardDictionary():
    
    fullDictionary = []
   

    input_text = open(r'input.txt', 'r').read()
    print(input_text)
    
  
    #first pass
    def findPatterns(startBound, indicator, endBound):
        # does not return anything, modifies toRet

        #doesnt work for things like Washington D.C.
        input_sentences = input_text.split(".")

        #blank is a blank format
        
        #iterates through every sentence  
        for j in range(len(input_sentences)):
            #sets regex, calls it to find word
            word = re.compile('(?<=' + startBound + ').*(?=' + indicator + ')')
            
            input_sentences[j] = ". " + input_sentences[j] 

            #finds definition
            definition = re.compile('(?<=' + indicator + ').*(?=' + endBound + ')')

            #finds all instances of format
            foundWords = word.findall(input_sentences[j], re.IGNORECASE)
            foundDefinitions = definition.findall(input_sentences[j], re.IGNORECASE)

            #loops through all word/definition pairs, appends to dictionary
            #must be same length
            for i in range(len(foundWords)):

                flashcard = {
                    'word': '',
                    'definition': ''
                }

                #makes dictionary/flashcard
                flashcard['word'] = foundWords[i]
                flashcard['definition'] = foundDefinitions[i]
                #appends pair to dictionary
                fullDictionary.append(flashcard)

                print(flashcard)

       
    def findKeywords():
        # does not return anything, modifies toRet
        pass
    

    findPatterns(". ", " is a ", ".*") #looks for "is a"
    findPatterns(". ", " has been ", ".*") #Looks for "has been"
    findPatterns(". ", " was a ", ".*") #Looks for "was a"
    
    ##FIZXXXXXX
    findPatterns("in December \d ", ", ", ".*") #Looks for "in December"
    
    return fullDictionary



def writeOutput(cardDict):
    pass
    #does not return anything, overwrites output.txt
    
    

