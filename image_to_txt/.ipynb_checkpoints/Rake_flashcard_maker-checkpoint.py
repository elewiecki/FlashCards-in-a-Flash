import nltk.data
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))
from nltk import tokenize
from operator import itemgetter
import math
from rake_nltk import Rake

def main():
    #this is an object that looks like 
    '''
    [[(9.0, 'infinitely many solutions'), (8.0, 'exactly one solution'), (4.0, 'linear equations'), (2.0, 'solution'), (1.0, 'system'), (1.0, '3'), (1.0, '2'), (1.0, '1')], [(8.25, 'replace one row'), (8.25, 'elementary row operations'), (8.0, 'interchange two rows'), (4.25, 'row .!'), (4.0, 'nonzero constant'), (2.25, 'row'), (2.0, 'interchange'), (1.0, 'sum'), (1.0, 'scaling'), (1.0, 'replacement'), (1.0, 'multiply'), (1.0, 'multiple'), (1.0, 'entries'), (1.0, 'another'), (1.0, '3'), (1.0, '2'), (1.0, '1')], 
    [(16.0, 'rarely contain standard punctuation'), (16.0, 'indexes within ir systems'), (14.666666666666666, 'natural numbers ). stop'), (14.0, 'keywords frequently contain multiple'), (9.5, 'manually assigned keywords'), (9.0, 'minimal lexical meaning'), (8.0, 'various text analyses'), (4.666666666666666, 'stop word'), (4.0, 'typically dropped'), (4.0, 'search tasks'), (4.0, 'one keyword'), (4.0, 'broadly used'), (4.0, 'aid users'), (3.8095238095238093, 'stop words'), (3.5, 'figure 1'), (2.5, 'frequently'), (2.0, 'analyses'), (1.5, '1'), (1.1428571428571428, 'words'), (1.1428571428571428, 'words'), (1.1428571428571428, 'words'), (1.1428571428571428, 'words'), (1.1428571428571428, 'words'), (1.1428571428571428, 'words'), (1.0, 'uninformative'), (1.0, 'set'), (1.0, 'reviewing'), (1.0, 'reasoning'), (1.0, 'rake'), (1.0, 'observation'), (1.0, 'meaningless'), (1.0, 'included'), (1.0, 'function'), (1.0, 'expectation'), (1.0, 'contains'), (1.0, 'considered'), (1.0, 'based'), (1.0, 'based'), (1.0, 'abstract')]] 
    
    or like this 
    [ [] [] [] ]
    
    '''

    rank_data = rank_most_imp_phrases("saved_defenitions.txt") #need the first the [][][1] and find the scentences for those
    
    for i in range (len(rank_data)):
        print("Next topic, next set of recomendations")
        for a in range (10):
            print("term: " + rank_data[i][a][1]+ "\n" + "Def : " + find_scentence(rank_data[i][a][1]) + "\n")
            print()
            #print(find_scentence(rank_data[i][a][1]))
            #print("This is the bs part next")
            #print(find_scentence(rank_data[i][0][1]))

# takes in all the possible screenshotted or copy pasted information for flashcards and returns their most important phrases
def rank_most_imp_phrases(filename):
    file = open(filename, 'r')
    flashcard_data = []
    r = Rake() #Rake object to use rake nltk method of picking most important phrases from a bunch of scentences.
    scentences = [] #empty init array that is populated by the for loop below and contains all the lines 
    i = 0
    for line in file:
        if line == "----------\n":
            r.extract_keywords_from_sentences(scentences)
            flashcard_data.append(r.get_ranked_phrases_with_scores())
            scentences = [] 
            continue
        scentences.append(line)
    return flashcard_data

#takes a string that you want to find the scentence it comes from saved_defenitions.txt
def find_scentence(search_string):
    data = split_data("saved_defenitions.txt")
    for obj in data:
        if search_string.casefold() in obj.casefold():
            scentences = split_string_into_scentences(obj)
            for scent in scentences:
                if search_string.casefold() in scent.casefold():
                    return scent
    return ""

#takes in all the data and returns an array which splits the data base on "----------\n"
def split_data(text_file_name):
    obj = ""
    file = open(text_file_name, 'r')
    obj_arr = []
    for line in file:
        if line == "----------\n":
            obj_arr.append(obj)
            obj = ""
            continue
        obj += line
    return obj_arr
        

# takes a string and returns an array data in which each element in a scentence in the input string
def split_string_into_scentences(string):
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    data = sent_detector.tokenize(string.strip()) 
    return data
if __name__ == "__main__":
    main()