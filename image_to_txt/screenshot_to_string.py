import pytesseract
from PIL import Image
import cv2 
from PIL import ImageGrab
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def main():

    usr_input = input("Please enter if you want to copy paste your paragraph, or provide a screenshot. Respond with ss for screenshot or cp for copypaste ")
    if usr_input == "ss" : 
        usr_input = input( "Please type your image name with .png at the end: ")
        string = convert_image_to_string(usr_input)
        
    elif usr_input == "cp":
        usr_input= input("Please paste your definition: ")
        string = usr_input
        save_to_file(usr_input)


def convert_image_to_data(image_name):
    image_data = pytesseract.image_to_data(image_name) 
    print(image_data)
    
def convert_image_to_string(image_name):
    image_string = pytesseract.image_to_string(image_name)
    image_string = image_string[:(len(image_string)) - 1] 
    save_to_file(image_string)
    return image_string

def save_to_file(string):
    string += "\n ---------- \n"
    text_file = open("saved_defenitions.txt", "a")
    text_file.write(string)
    text_file.close()

if __name__ == "__main__":
    main()