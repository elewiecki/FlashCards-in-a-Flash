'''
use selenium


'''

from selenium import webdriver

#dummy data
cardDict = {
    't1' : 'd1',
    't2' : 'd2',
    't3' : 'd3',
    't4' : 'd4',
    't5' : 'd5',
    't6' : 'd6',
    't7' : 'd7',
    't8' : 'd8',
    't9' : 'd9',
    't10' : 'd10',
}

cards = 't1\d1\nt2\d2\nt3\d3\nt4\d4\nt5\d5\nt6\d6\nt7\d7\nt8\d8\nt9\d9\nt10\d10\n'

class QuizletBot():
    def __init__(self, cards):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        self.cards = cards
        
    #def login(self):
    #def createFlashcards(self):
        #self.driver.get('https://quizlet.com/create-set')