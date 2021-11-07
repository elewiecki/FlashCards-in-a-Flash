import quizletbot as qb
import model as m



#Hackathon123!
def main():
    #first user copy pastes into input.txt
    m.execute()
    cards = open('output.txt', 'r').read()
    bot = qb.QuizletBot(cards)
    bot.login()
    bot.createFlashcards()

if __name__ == "__main__":
    main()









