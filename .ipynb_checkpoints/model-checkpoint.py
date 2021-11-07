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

def execute():
    writeOutput(createCardDictionary())



def createCardDictionary():
   
    fullDictionary = []
    words = []

    #input is in format thing then 10 dashes
    input_text = open(r'image_to_txt\saved_defenitions.txt', 'r', encoding='utf8').read()
    
    
    input_text = input_text.replace('\n', ' ')
    
    input_sentences = re.split("(?<=[^A-Z])\.|\?[^a-zA-Z]" , input_text) #problem: acronyms. Solution: nltk library, would have to load into repo or something
    
    
    for j in range(len(input_sentences)):
        input_sentences[j] = "\. " + input_sentences[j]
    
    #creates flashcard and adds to dictionary
    def  appendCardToDictionary(foundDefinitions, foundWords):
        
        for i in range(min(len(foundDefinitions), len(foundWords))):
            if len(foundDefinitions[i]) <= 2:
                continue


            flashcard = {
                 'word': '',
                  'definition': ''
            }

             #makes dictionary/flashcard
            
            newWord = foundWords[i].lstrip()
            newDefinition = foundDefinitions[i].lstrip()
            if newWord not in words:
                flashcard['word'] = newWord
                flashcard['definition'] = newDefinition
                #appends pair to dictionary
                fullDictionary.append(flashcard)
                words.append(newWord)       
                print(flashcard)  
            
            
    #Works in format "[start indicator] [word] [indicator phrase] [definition] [end indicator]"
    def findBoundedIndicator(startBound, indicator, endBound):
        # does not return anything, modifies fullDictionary
        
        #iterates through every sentence  
        for j in range(len(input_sentences)):
            #sets regex, calls it to find word
            word = re.compile('(?<=' + startBound + ').*(?=' + indicator + ')')
        

            #finds definition
            definition = re.compile('(?<=' + indicator + ').*(?=' + endBound + ')')

            #finds all instances of format
            foundWords = word.findall(input_sentences[j], re.IGNORECASE)
            foundDefinitions = definition.findall(input_sentences[j], re.IGNORECASE)

            #loops through all word/definition pairs, appends to dictionary
            #must be same length
            appendCardToDictionary(foundDefinitions, foundWords)

    #works with format [indicator] [definition] [endBound]
    def findIndicatorToEndBound(indicator, endBound):
        # does not return anything, modifies toRet
        
        #iterates through every sentence  
        for j in range(len(input_sentences)):

            #finds definition
            definition = re.compile('(?<=' + indicator + ').*(?=' + endBound + ')')

            #finds all instances of format
            foundWords = re.findall(indicator, input_sentences[j], re.IGNORECASE)
            foundDefinitions = definition.findall(input_sentences[j], re.IGNORECASE)

            #loops through all word/definition pairs, appends to dictionary
            #must be same length
            appendCardToDictionary(foundDefinitions, foundWords)

       
    def findKeywords():
        # does not return anything, modifies toRet
        pass
    

    findBoundedIndicator(". ", "(?<!What)(?<!Why)(?<!How)(?<!When)(?<!Where)(?<!Who)(?<!It)(?<!That)(?<!This)(?<!He)(?<!Her)(?<!:) is a ", ".*") #looks for "is a"
    findBoundedIndicator(". ", "(?<!What)(?<!Why)(?<!How)(?<!When)(?<!Where)(?<!Who)(?<!It)(?<!That)(?<!This)(?<!He)(?<!Her) is an ", ".*") #looks for "is a"
    findBoundedIndicator(". ", " has been ", ".*") #Looks for "has been"
    findBoundedIndicator(". ", " was a ", ".*") #Looks for "was a"
    findBoundedIndicator(". ", ": ", ".*") #looks for :
    findBoundedIndicator(". ", "(?<!What)(?<!Why)(?<!How)(?<!When)(?<!Where)(?<!Who)(?<!It)(?<!That)(?<!This)(?<!He)(?<!Her) is defined as", ".*") 
    findBoundedIndicator(". ", "(?<!What)(?<!Why)(?<!How)(?<!When)(?<!Where)(?<!Who)(?<!It)(?<!That)(?<!This)(?<!He)(?<!Her) is called ", ".*") 
    findBoundedIndicator("If ", ", then ", ".*")
  
    findIndicatorToEndBound("(?<=\D)\d\d\d\d(?=\D)", ".*") #Looks for year


     
    print(len(fullDictionary))
    return fullDictionary



def writeOutput(cardDict):
    
    output_text = open("output.txt","w", encoding='utf8')
    for i in range(len(cardDict)):
        output_text.write(cardDict[i]["word"] + "@@@" + cardDict[i]["definition"] + "\n")

    output_text.close()
    #does not return anything, overwrites output.txt
    
    

