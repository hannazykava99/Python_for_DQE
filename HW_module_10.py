from HW_module_6 import News, Advertisement, Divination, FromAnotherSource
from HW_module_7 import CsvTasks
from HW_module_8 import FromJson
from HW_module_9 import FromXml
import os
import re
import sqlite3


class DBInsert:

    def convert_to_tuple(self, list):
        return tuple(i for i in list)

    def inserting(self, lst):
        conn = sqlite3.connect('Result.db')
        cursor = conn.cursor()
        # cursor.execute('DROP TABLE news')
        # cursor.execute('DROP TABLE advertisement')
        # cursor.execute('DROP TABLE divination')
        # conn.commit()
        cursor.execute('CREATE TABLE IF NOT EXISTS news (news_text text, city text, date text)')
        cursor.execute('CREATE TABLE IF NOT EXISTS advertisement (ad_text text, actual_date text, days_left text)')
        cursor.execute('CREATE TABLE IF NOT EXISTS divination (question text, answer text, comment text)')
        conn.commit()

        new_list = list(lst)

        # remove "\n" symbols
        for el in new_list:
            re.sub('\n', '', el)
        if new_list[0] == 'News:':
            new_list[1] = new_list[1].replace('\n', '')
            split = new_list[2].split(', ')
            new_list[2] = split[0]
            new_list.append(split[1].replace('\n', ''))
            tuple_result = self.convert_to_tuple(new_list[1:4])
            cursor.execute('SELECT * FROM news')
            result = cursor.fetchall()
            if tuple_result in result:
                print(f'We already have such record in "news" table: {tuple_result}')
            else:
                cursor.execute('INSERT INTO news VALUES (?, ?, ?)', tuple_result)
        elif new_list[0] == 'Private Ad:':
            new_list[1] = new_list[1].replace('\n', '')
            split = new_list[2].split(', ')
            new_list[2] = split[0]
            new_list.append(split[1].replace('\n', ''))
            tuple_result = self.convert_to_tuple(new_list[1:4])
            cursor.execute('SELECT * FROM advertisement')
            result = cursor.fetchall()
            if tuple_result in result:
                print(f'We already have such record in "advertisement" table: {tuple_result}')
            else:
                cursor.execute('INSERT INTO advertisement VALUES (?, ?, ?)', tuple_result)
        elif new_list[0] == 'Question-divination:':
            new_list[1], new_list[2], new_list[3] = new_list[1].replace('\n', ''), new_list[2].replace('\n', ''), new_list[3].replace('\n', '')
            tuple_result = self.convert_to_tuple(new_list[1:4])
            cursor.execute('SELECT * FROM divination')
            result = cursor.fetchall()
            if tuple_result in result:
                print(f'We already have such record in "divination" table: {tuple_result}')
            else:
                cursor.execute('INSERT INTO divination VALUES (?, ?, ?)', tuple_result)

        conn.commit()
        cursor.close()
        conn.close()

    def selecting_all_tables(self):

        conn = sqlite3.connect('Result.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM news;")
        result = cursor.fetchall()
        print('"News" table:', result)
        cursor.execute("SELECT * FROM advertisement;")
        result = cursor.fetchall()
        print('"Advertisement" table:', result)
        cursor.execute("SELECT * FROM divination;")
        result = cursor.fetchall()
        print('"Divination" table:', result)

        cursor.close()
        conn.close()



if __name__ == "__main__":
    # ask a user what data he wants to print and then call a class and insert the data into file using inserting method
    while True:
        print('What do you want to print?', '1 - News', '2 - Private Ad', '3 - Divination', '4 - Add data from another .txt file', '5 - Add data from .json file', '6 - Add data from .xml file', '7 - Nothing', sep='\n')
        reply = input('Choose the appropriate number: ')
        print()
        if reply == '1':
            data = News().publishing()
            DBInsert().inserting(data)
            News().formatting(data)
            News().inserting(data)
            print('The news is published in Text.txt file')
            print('The news is published in Result.db file if we don\'t have it previously\n')
        elif reply == '2':
            data = Advertisement().publishing()
            DBInsert().inserting(data)
            Advertisement().formatting(data)
            Advertisement().inserting(data)
            print('The advertisement is published in Text.txt file')
            print('The advertisement is published in Result.db file if we don\'t have it previously\n')
        elif reply == '3':
            data = Divination().publishing()
            DBInsert().inserting(data)
            Divination().formatting(data)
            Divination().inserting(data)
            print('The divination is published in Text.txt file')
            print('The divination is published in Result.db file if we don\'t have it previously\n')
        elif reply == '4':
            data, path_for_remove = FromAnotherSource().publishing()
            if data == 'Empty':
                print('Something went wrong with insertion data from the .txt file. Please fix the format of incoming file and try again\n')
            else:
                for d in data:
                    DBInsert().inserting(d)
                    FromAnotherSource().formatting(d)
                    FromAnotherSource().inserting(d)
                print('The data from this file is published in Text.txt file')
                print(f'This file {path_for_remove} will be removed now')
                os.remove(path_for_remove)
                print('The records are published in Result.db file if we don\'t have them previously\n')
        elif reply == '5':
            data, path_for_remove = FromJson().publishing()
            if data == 'Empty':
                print('Something went wrong with insertion data from the .json file. Please fix the format of incoming file and try again\n')
            else:
                for d in data:
                    DBInsert().inserting(d)
                    FromJson().formatting(d)
                    FromJson().inserting(d)
                print('The data from this file is published in Text.txt file')
                print(f'This file {path_for_remove} will be removed now')
                os.remove(path_for_remove)
                print('The records are published in Result.db file if we don\'t have them previously\n')
        elif reply == '6':
            data, path_for_remove = FromXml().publishing()
            if data == 'Empty':
                print('Something went wrong with insertion data from the .xml file. Please fix the format of incoming file and try again\n')
            else:
                for d in data:
                    DBInsert().inserting(d)
                    FromXml().formatting(d)
                    FromXml().inserting(d)
                print('The data from this file is published in Text.txt file')
                print(f'This file {path_for_remove} will be removed now')
                os.remove(path_for_remove)
                print('The records are published in Result.db file if we don\'t have them previously\n')
        elif reply == '7':
            print('You have updated the Text.txt file. The program is stopped')
            CsvTasks().word_count()
            CsvTasks().letter_count()
            print('Word_count.csv and letter_count.csv files are updated')
            break
        else:
            print('Try again')

# DBInsert().selecting_all_tables()

