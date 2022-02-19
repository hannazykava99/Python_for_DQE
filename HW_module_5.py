from datetime import datetime, date
from random import randint


class FileInsert:
    text = None

    def inserting(self, text):
        self.text = text
        with open("Text.txt", "a", encoding='utf-8') as file:
            for line in self.text:
                file.write(line + '\n')


class News(FileInsert):

    def publishing(self):
        data = []
        data.append('\nNews: -----------------------------')
        news = input('Enter the text of your news: ')
        city = input('Enter the city: ')
        data.append(news)
        data.append(city.capitalize() + ', ' + str(datetime.now().strftime("%d/%m/%Y %H:%M")))
        data.append('-----------------------------------')
        return data


class Advertisement(FileInsert):
    current_day = date.today()
    expiration_date = date.today()
    isTrue = True
    data = []

    def publishing(self):
        self.data = []
        ad = input('Enter the text of the advertisement: ')
        while self.isTrue:
            try:
                d = input('Enter expiration day of the advertisement in numeric format: ')
                m = input('Enter expiration month of the advertisement in numeric format: ')
                y = input('Enter expiration year of the advertisement in numeric format: ')
                self.expiration_date = date(int(y), int(m), int(d))
                self.isTrue = False
            except ValueError:
                print("This date doesn't exist. Try again")
            except OverflowError:
                print("This date doesn't exist. Try again")
        deadline = self.expiration_date
        if self.current_day > deadline:
            comment = "Advertising is outdated"
        elif self.current_day == deadline:
            comment = "Today is the last day of the advertisement"
        else:
            diff = deadline - self.current_day
            if diff.days == 1:
                comment = str(diff.days) + ' day left'
            else:
                comment = str(diff.days) + ' days left'
        self.data.append('\nPrivate Ad: -----------------------')
        self.data.append(ad)
        last_string = 'Actual until: ' + deadline.strftime("%d/%m/%Y") + ', ' + comment
        self.data.append(last_string)
        self.data.append('-----------------------------------')
        return self.data


class Divination(FileInsert):
    data = []
    isTrue = True

    def publishing(self):
        self.data = []
        self.data.append('\nQuestion-divination: --------------')
        answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'As I see it, yes',
                        'Most likely', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
                        'Don\'t count on it', 'My reply is no', 'My sources say no', 'Very doubtful']
        while self.isTrue:
            question = input('Your question is: ')
            if question[-1] == '?':
                self.isTrue = False
                self.data.append(question)
            else:
                print('It seems you didn\'t write a question')
        self.data.append(answers[randint(0, len(answers) - 1)])
        self.data.append('I hope that helped!')
        self.data.append('-----------------------------------')
        return self.data


while True:
    print('What do you want to print?', '1 - News', '2 - Private Ad', '3 - Divination', '4 - Nothing', sep='\n')
    reply = input('Choose the appropriate number: ')
    if reply == '1':
        data = News().publishing()
        News().inserting(data)
    elif reply == '2':
        data = Advertisement().publishing()
        Advertisement().inserting(data)
    elif reply == '3':
        data = Divination().publishing()
        Divination().inserting(data)
    elif reply == '4':
        print('Stop')
        break
    else:
        print('Try again')
