import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
stop_words = set(stopwords.words('english'))
from nltk import tokenize
from operator import itemgetter
import math
from rake_nltk import Rake

def main():
    file = open("saved_defenitions.txt", "r")
    arr = []
    for line in file:
        arr.append(line)
    r = Rake()
    x = ["In developing RAKE, our motivation has been to develop a keyword extraction method that is extremely efﬁcient, operates on individual documents to enable application to dynamic collections, is easily applied to new domains, and operates well on multiple types of documents, particularly those that do not follow speciﬁcgrammar conventions. Figure 1.1 contains the title and text for a typical abstract,as well as its manually assigned keywords"]
    r.extract_keywords_from_sentences(x)
    print(r.get_ranked_phrases_with_scores())

if __name__ == "__main__":
    main()