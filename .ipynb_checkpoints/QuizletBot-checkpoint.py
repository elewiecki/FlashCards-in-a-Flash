'''
use selenium


'''

from selenium import webdriver


class QuizletBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
