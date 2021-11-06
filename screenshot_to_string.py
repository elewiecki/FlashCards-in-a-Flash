import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def main():
    usr_image_input = input("Please enter the name of the image you want to convert: ")
    convert_image_to_string(usr_image_input)
    

def convert_image_to_string(image_name):
    image_string = pytesseract.image_to_string(image_name)
    save_to_file(image_string + "\n ---------- \n")
    print(image_string)

def save_to_file(string):
    text_file = open("saved_defenitions.txt", "a")
    text_file.write(string)
    text_file.close()

if __name__ == "__main__":
    main()