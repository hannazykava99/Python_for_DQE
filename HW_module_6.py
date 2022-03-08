from datetime import datetime, date
from random import randint
from HW_module_4_part_2 import letter_case_normalization as normalize
import os

class FileInsert:

   # create a method which formats the text according to requirements
    def formatting(self, text):
        text[0] = text[0] + ('' + '-' * (40 - len(text[0]))) + '\n'
        text.append(('-' * 40) + '\n\n')

    # create a method which inserts the formatted text into text file (create this file if necessary or add new information if file exists)
    def inserting(self, text):
        # open, populate and close the file
        with open("Text.txt", "a", encoding='utf-8') as file:
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
        # print(val)
        return val

    # create a method which checks that we don't leave the input field empty (if it is empty - try again)
    def input_string(self, text):
        while True:
            val = input(text)
            if len(val) > 0:
                break
            else:
                print('Enter something, please')
        # print(val)
        return val



class News(FileInsert, CheckInput):

    # create a method which creates a news (text, city, current date + time)
    def publishing(self):
        data = []
        data.append('News:')
        news = self.input_string('Enter the text of your news: ')
        city = self.input_string('Enter the city: ')
        data.append(news + "\n")
        data.append(city.capitalize() + ', ' + str(datetime.now().strftime("%d/%m/%Y %H:%M")) + "\n")
        # print(data)
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
        # print(data)
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
        # print(data)
        return data


class FromAnotherSource(FileInsert):

    # create a method which makes another directories and reads a file from that directory OR use the default one
    def read_file(self):
        original_path = os.path.dirname(os.path.realpath(__file__))
        print(f'Your default directory is "{os.getcwd()}"')
        answer = CheckInput().input_int(
            f'If you want to ingest your file from default directory - enter 1, if you want to change it - enter 2: ')
        if answer == 1:
            while True:
                try:
                    file_name = CheckInput().input_string('Enter the file name with its format: ')
                    with open(file_name, "r", encoding='utf-8') as source:
                        f_contents = source.readlines()
                    print('Okay, such file exists')
                    path_for_remove = str(file_name)
                    break
                except FileNotFoundError:
                    print('No file with such name. Try again')
                except PermissionError:
                    print('No file with such name. Try again')
        elif answer == 2:
            while True:
                try:
                    change_path = input('Enter the file path: ')
                    if not os.path.isdir(change_path):
                        os.mkdir(change_path)
                    os.chdir(change_path)
                    print(f'Now you directory is "{os.getcwd()}"')
                    break
                except SyntaxError:
                    print('You made a mistake. Try again')
                except FileNotFoundError:
                    print('You made a mistake. Try again')
            while True:
                try:
                    file_name = CheckInput().input_string('Enter the file name with its format: ')
                    with open(file_name, "r", encoding='utf-8') as source:
                        f_contents = source.readlines()
                    print('Such file exists')
                    path_for_remove = os.path.join(str(change_path), str(file_name))
                    os.chdir(original_path)
                    break
                except FileNotFoundError:
                    print('No file with such name. Try again')
                except PermissionError:
                    print('No file with such name. Try again')
        else:
            print('Try again')
        return f_contents, path_for_remove

    # create a method which accumulate all data pieces from another file
    def publishing(self):
        f_contents, path_for_remove = self.read_file()
        i = 0
        insert_into_file = []
        while i < len(f_contents):
            try:
                data = []
                if f_contents[i] == 'News:\n' and len(f_contents[i+1]) > 1 and len(f_contents[i+2]) > 1 and f_contents[i+1][-1] == '\n' and f_contents[i+2][-1] == '\n' and f_contents[i+3] == '\n':
                    data.append('News:')
                    data.append(normalize(f_contents[i+1]))
                    data.append((f_contents[i+2]).capitalize())
                    # print(data)
                    insert_into_file.append(data)
                    i += 4
                elif f_contents[i] == 'Private Ad:\n' and len(f_contents[i+1]) > 1 and len(f_contents[i+2]) > 1 and f_contents[i+1][-1] == '\n' and f_contents[i+2][-1] == '\n' and f_contents[i+3] == '\n':
                    data.append('Private Ad:')
                    data.append(normalize(f_contents[i+1]))
                    data.append(f_contents[i+2])
                    # print(data)
                    insert_into_file.append(data)
                    i += 4
                elif f_contents[i] == 'Question-divination:\n' and len(f_contents[i+1]) > 1 and len(f_contents[i+2]) > 1 and len(f_contents[i+3]) > 1 and f_contents[i+1][-1] == '\n' and f_contents[i+2][-1] == '\n' and f_contents[i+3][-1] == '\n' and f_contents[i+4] == '\n':
                    data.append('Question-divination:')
                    data.append(normalize(f_contents[i+1]))
                    data.append(f_contents[i+2])
                    data.append(f_contents[i+3])
                    # print(data)
                    insert_into_file.append(data)
                    i += 5
                else:
                    insert_into_file = 'Empty'
                    break
            except IndexError:
                insert_into_file = 'Empty'
                break
        # print(insert_into_file)
        return insert_into_file, path_for_remove


if __name__ == "__main__":
    # ask a user what data he wants to print and then call a class and insert the data into file using inserting method
    while True:
        print('What do you want to print?', '1 - News', '2 - Private Ad', '3 - Divination', '4 - Add data from another file', '5 - Nothing', sep='\n')
        reply = input('Choose the appropriate number: ')
        print()
        if reply == '1':
            data = News().publishing()
            News().formatting(data)
            News().inserting(data)
            print('The news is published in Text.txt file\n')
        elif reply == '2':
            data = Advertisement().publishing()
            Advertisement().formatting(data)
            Advertisement().inserting(data)
            print('The advertisement is published in Text.txt file\n')
        elif reply == '3':
            data = Divination().publishing()
            Divination().formatting(data)
            Divination().inserting(data)
            print('The divination is published in Text.txt file\n')
        elif reply == '4':
            # check if we can successfully process the file then delete it
            data, path_for_remove = FromAnotherSource().publishing()
            if data == 'Empty':
                print('Something went wrong with insertion data from the file. Please fix the format of incoming file and try again\n')
            else:
                for d in data:
                    FromAnotherSource().formatting(d)
                    FromAnotherSource().inserting(d)
                print('The data from this file is published in Text.txt file')
                print(f'This file {path_for_remove} will be removed now\n')
                # os.remove(path_for_remove)
        elif reply == '5':
            print('You have updated the document. The program is stopped.')
            break
        else:
            print('Try again')
