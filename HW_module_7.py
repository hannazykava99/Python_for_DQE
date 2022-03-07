from HW_module_6 import News, Advertisement, Divination, FromAnotherSource
import re
import csv
import os
from string import ascii_lowercase


class CsvTasks:

    # create a method which calculate letter-count
    def letter_count(self):

        with open("Text.txt", "r", encoding='utf-8') as file:
            txt = file.read()

        elements = []
        for i in txt:
            if i not in (' ', "\n", "\t"):
                elements.append(i)

        all_count = len(elements)

        list_of_dict = []
        for b in ascii_lowercase:
            count_all = 0
            count_upper = 0
            dict = {}
            for el in elements:
                if el.lower() == b:
                    count_all += 1
                if el == b.upper():
                    count_upper += 1
                dict.update({'letter': b, 'count_all': count_all, 'count_uppercase': count_upper,
                             'percentage': round((count_all / all_count) * 100, 2)})
            list_of_dict.append(dict)

        with open('letter_count.csv', "w", newline="") as csvfile:
            columns = ["letter", "count_all", "count_uppercase", "percentage"]
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writeheader()
            writer.writerows(list_of_dict)


    # create a method which calculate word-count (all words are preprocessed in lowercase)
    def word_count(self):

        with open("Text.txt", "r", encoding='utf-8') as file:
            txt = file.read()

        all_words = re.findall("\w+[^ ,!?.:/\n]?\w*", txt)

        words_lowercase = []
        for i in all_words:
            words_lowercase.append(i.lower())

        words_count = {}
        for i in words_lowercase:
            if i in words_count:
                words_count[i] += 1
            else:
                words_count[i] = 1

        with open('word_count.csv', 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=",", lineterminator="\r")
            for key, value in words_count.items():
                writer.writerow([key, value])




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
            data, path_for_remove = FromAnotherSource().publishing()
            if data == 'Empty':
                print('Something went wrong with insertion data from the file. Please fix the format of incoming file and try again\n')
            else:
                for d in data:
                    FromAnotherSource().formatting(d)
                    FromAnotherSource().inserting(d)
                print('The data from this file is published in Text.txt file')
                print(f'This file {path_for_remove} will be removed now\n')
                os.remove(path_for_remove)
        elif reply == '5':
            print('You have updated the document. The program is stopped.')
            CsvTasks().word_count()
            CsvTasks().letter_count()
            print('Word_count.csv and letter.csv files are updated')
            break
        else:
            print('Try again')


