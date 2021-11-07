import pytesseract
from PIL import Image
import cv2 
from PIL import ImageGrab
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def main():

    # simple if else that get the information of whether the user is copy pasting or using screenshots
    usr_input = input("Please enter if you want to copy paste your paragraph, or provide a screenshot. Respond with ss for screenshot or cp for copypaste ")
    if usr_input == "ss" : 
        usr_input = input( "Please type your image name with .png at the end: ")
        string = convert_image_to_string(usr_input)
        
    elif usr_input == "cp":
        usr_input= input("Please paste your definition: ")
        string = usr_input
        save_to_file(usr_input)


# uses pytesseract to convert an image into text data with attributes that I dont quite understand
def convert_image_to_data(image_name):
    image_data = pytesseract.image_to_data(image_name) 
    print(image_data)
    
#Takes image name in the form of a string that looks like "abcd.png"
#Returns a string of the text found in the image, using pytesseract to convert the image to the text 
#It also pushed the text found in the image to saved_defenitions.txt
def convert_image_to_string(image_name):
    image_string = pytesseract.image_to_string(image_name)
    image_string = image_string[:(len(image_string)) - 1] #removes the last element as it has consistent noise from pytesseract reading the immage text
    save_to_file(image_string)
    return image_string

#takes in a string to save to saved_defenitions.txt
#returns None
#Saves the string to saved_defenitions.txt and appends "\n ---------- \n" at the end of the file to distinguish between entires 
def save_to_file(string):
    string += "\n" +  "----------" +  "\n" 
    text_file = open("saved_defenitions.txt", "a") #written with access mode to allow appending
    text_file.write(string)
    text_file.close()

if __name__ == "__main__":
    main()