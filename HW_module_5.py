from datetime import datetime, date
from random import randint


class FileInsert:

   # create a method which formats the text according to requirements
    def formatting(self, text):
        text[0] = text[0] + ('' + '-' * (40 - len(text[0]))) + '\n'
        text.append(('-' * 40) + '\n\n')

    # create a method which inserts the formatted text into text file (create this file if necessary or add new information if file exists)
    def inserting(self, text):
        # open, populate and close the file
        with open("Text.txt", "a", encoding='utf-8') as file:
            self.formatting(text)
            for line in text:
                file.write(line)


class CheckInput:

    # create a method which checks that we insert only numerical values (if not - try again)
    def input_int(self, text):
        while True:
            try:
                val = int(input(text))
                break
            except:
                print('Enter a numeric value, please')
        print(val)
        return val

    # create a method which checks that we don't leave the input field empty (if it is empty - try again)
    def input_string(self, text):
        while True:
            val = input(text)
            if len(val) > 0:
                break
            else:
                print('Enter something, please')
        print(val)
        return val



class News(FileInsert, CheckInput):

    # create a method which creates a news (text, city, current date + time)
    def publishing(self):
        data = []
        data.append('News: ')
        news = self.input_string('Enter the text of your news: ')
        city = self.input_string('Enter the city:')
        data.append(news + "\n")
        data.append(city.capitalize() + ', ' + str(datetime.now().strftime("%d/%m/%Y %H:%M")) + "\n")
        print(data)
        return data


class Advertisement(FileInsert, CheckInput):

    # create a method which creates an advertisement (text, expiration day, how many days left)
    def publishing(self):
        data = []
        ad = self.input_string('Enter the text of the advertisement: ')
        is_true = True
        # set the expiration date by default as current day
        expiration_date = date.today()
        while is_true:
            try:
                d = self.input_int('Enter expiration day of the advertisement in numeric format: ')
                m = self.input_int('Enter expiration month of the advertisement in numeric format: ')
                y = self.input_int('Enter expiration year of the advertisement in numeric format: ')
                expiration_date = date(y, m, d)
                is_true = False
            except ValueError:
                print("This date doesn't exist. Try again")
            except OverflowError:
                print("This date doesn't exist. Try again")
        if expiration_date < date.today():
            comment = "Advertising is outdated"
        elif expiration_date == date.today():
            comment = "Today is the last day of the advertisement"
        else:
            diff = expiration_date - date.today()
            if diff.days == 1:
                comment = str(diff.days) + ' day left'
            else:
                comment = str(diff.days) + ' days left'
        data.append('Private Ad:')
        data.append(ad + "\n")
        data.append('Actual until: ' + expiration_date.strftime("%d/%m/%Y") + ', ' + comment + "\n")
        print(data)
        return data


class Divination(FileInsert, CheckInput):

    # create a method which creates a divination (user asks a question and gets an answer)
    def publishing(self):
        data = []
        data.append('Question-divination:')
        answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'As I see it, yes',
                        'Most likely', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
                        'Don\'t count on it', 'My reply is no', 'My sources say no', 'Very doubtful']
        is_true = True
        while is_true:
            question = self.input_string('Your question is: ')
            # check that user ask a question: the input should contain "?" at the end of sentence
            if question[-1] == '?':
                is_true = False
                data.append(question + "\n")
            else:
                print('It seems you didn\'t write a question')
        # generate a divination using random lib
        data.append(answers[randint(0, len(answers) - 1)] + "\n")
        data.append('I hope that helped!' + "\n")
        print(data)
        return data


if __name__ == "__main__":
    # ask a user what data he wants to print and then call a class and insert the data into file using inserting method
    while True:
        print('What do you want to print?', '1 - News', '2 - Private Ad', '3 - Divination', '4 - Nothing', sep='\n')
        reply = input('Choose the appropriate number: ')
        if reply == '1':
            data = News().publishing()
            News().inserting(data)
            print('The news is published in Text.txt file\n')
        elif reply == '2':
            data = Advertisement().publishing()
            Advertisement().inserting(data)
            print('The advertisement is published in Text.txt file\n')
        elif reply == '3':
            data = Divination().publishing()
            Divination().inserting(data)
            print('The divination is published in Text.txt file\n')
        elif reply == '4':
            print('Stop')
            break
        else:
            print('Try again')


