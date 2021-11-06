'''
use selenium


'''

from selenium import webdriver
from time import sleep
import secrets

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

cards = 't1\td1\nt2\td2\nt3\td3\nt4\td4\nt5\td5\nt6\td6\nt7\td7\nt8\td8\nt9\td9\nt10\td10\n'

#/Users/joshuashen/Downloads/chromedriver
class QuizletBot():
    def __init__(self, cards):
        self.driver = webdriver.Chrome(executable_path = '/Users/joshuashen/Downloads/chromedriver')
        self.cards = cards
        
    def login(self):
        self.driver.get('https://quizlet.com/create-set')
        
        qlogin_btn = self.driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/form/div[6]/div/span/span/button')
        qlogin_btn.click()
        
        username_in = self.driver.find_element_by_xpath('//*[@id="username"]')
        username_in.send_keys(secrets.username)
        password_in = self.driver.find_element_by_xpath('//*[@id="password"]')
        password_in.send_keys(secrets.password)
        
        login_btn = self.driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/form/button')
        login_btn.click()
        
        return
    
    def createFlashcards(self):
        self.driver.get('https://quizlet.com/create-set')
        return