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

cards = 't1,d1\nt2,d2\nt3,d3\nt4,d4\nt5,d5\nt6,d6\nt7,d7\nt8,d8\nt9,d9\nt10,d10\n'

#/Users/joshuashen/Downloads/chromedriver
class QuizletBot():
    def __init__(self, cards, title):
        self.driver = webdriver.Chrome(executable_path = '/Users/joshuashen/Downloads/chromedriver')
        self.cards = cards
        self.title = title
        
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
        sleep(2)
        x_btn = self.driver.find_element_by_xpath('/html/body/div[13]/div/div[1]/div/button')
        x_btn.click()
        
        import_btn = self.driver.find_element_by_xpath('//*[@id="SetPageTarget"]/div/div[1]/div[3]/div/a')
        import_btn.click()
        
        comma_btn = self.driver.find_element_by_xpath('//*[@id="SetPageTarget"]/div/div[3]/div[1]/div/form/div[2]/div[1]/div/label[2]/span[1]')
        comma_btn.click()
        
        data_in = self.driver.find_element_by_xpath('//*[@id="SetPageTarget"]/div/div[3]/div[1]/div/form/textarea')
        data_in.send_keys(cards)
        
        import_btn2 = self.driver.find_element_by_xpath('//*[@id="SetPageTarget"]/div/div[3]/div[1]/div/form/div[1]/button')
        import_btn2.click()
        
        title_in = self.driver.find_element_by_xpath('//*[@id="SetPageTarget"]/div/div[1]/div[2]/div/div[1]/div/label/input')
        title_in.send_keys(self.title)
        
        create_btn = self.driver.find_element_by_xpath('//*[@id="SetPageTarget"]/div/div[2]/div/div/div[2]/div/button/span/span')
        create_btn.click()
        
        
        
        
        return