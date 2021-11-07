# Flashcards in a Flash
##### Created by Josh Shen, Emmet Lewiecki, Ben Chou, Srinanda Yallapragada, Frank Chiu, and Vibhu Mogalapalli

![logo here](readme_images/logo.png)

If you're anything like us, you tend to procrastinate and have to study lots of material on a time crunch. When it comes to studying terms and definitions in a textbook, the process is pretty straightforward. **Flashcards in a Flash** automates this process by creating a flashcard set in Quizlet based on term and definition pairs that it finds. This is a massive improvement over having to comb through a textbook manually, identifying flashcard pairs, and then creating flashcards on Quizlet one-by-one yourself. Let **Flashcards in a Flash** do the heavy lifting so that you can focus on learning and review!

## Setup
Clone this repository to a local directory. Refer to [GitHub Pages](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) for more guidance if needed.

Next, you should install the necessary packages to run **main.py**: *selenium*, *pytesseract*, and *tkinter*. You can install these using **pip**:
- `pip install selenium`
- `pip install pytesseract`
- `pip install tk`

You will also need to install a chrome driver for **quizletbot.py** to be able to run. To do this, go to [WebDriver for Chrome](https://chromedriver.chromium.org/downloads) download page and install a version that matches your version of Chrome. This should give you a zip file, which, when unzipped, will create a **chromedriver.exe** file. Save the path of this file and paste it into *line 15* of **quizletbot.py** such that the line now reads as 

`self.driver = webdriver.Chrome(executable_path = 'chromedriver_path')`

Now your setup is done!

## Running the Code
To run the code, run **main.py**. This will open up a new Graphical User Interface window where you can copy/paste in the text that you want to use, or the file path of the image you want to use.

![image here](readme_images/gui.png)

Upon submitting text or an image, a new Chrome window should open and it will automatically go through the Quizlet interface to create your new flashcard set. 

![image here](readme_images/quizlet.png)

This process should take about 30 seconds, depending on the size of your input. Enjoy!

## Future Plans
- Improve our Natural Language Processing model to create more accurate flashcard pairs
- Create a website with an improved user interface
- Create an actual Quizlet API or find another workaround to programmatically interact Quizlet without using web driver


## Notes
This project was created for HackUMass 1001

If you have any questions or comments email us at jlshen@umass.edu

If we end up making a website, it will be hosted at https://flashcardsinaflash.tech/

Any future video content related to this project will be on the [Flashcards in a Flash](https://www.youtube.com/channel/UCkZHDzPeojOGCsy17b2PG2w) channel
