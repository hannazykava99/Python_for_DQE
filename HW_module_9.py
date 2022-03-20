from HW_module_6 import News, Advertisement, Divination, FromAnotherSource, FileInsert, CheckInput
from HW_module_7 import CsvTasks
from HW_module_8 import FromJson
import os
import xml.etree.ElementTree as et


class FromXml(FileInsert):

    def read_file(self):
        original_path = os.path.dirname(os.path.realpath(__file__))
        print(f'Your default directory is "{os.getcwd()}"')
        is_true = True
        while is_true:
            answer = CheckInput().input_int(
                f'If you want to ingest your file from default directory - enter 1, if you want to change it - enter 2: ')
            if answer == 1:
                while True:
                    try:
                        file_name = CheckInput().input_string('Enter the file name with its format: ')
                        xml_file = et.parse(file_name)
                        print('Okay, such file exists')
                        path_for_remove = str(file_name)
                        is_true = False
                        break
                    except FileNotFoundError:
                        print('No file with such name. Try again')
                    except PermissionError:
                        print('No file with such name. Try again')
                    except et.ParseError:
                        print('Incorrect file .xml structure')
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
                        xml_file = et.parse(file_name)
                        print('Okay, such file exists')
                        path_for_remove = os.path.join(str(change_path), str(file_name))
                        os.chdir(original_path)
                        is_true = False
                        break
                    except FileNotFoundError:
                        print('No file with such name. Try again')
                    except PermissionError:
                        print('No file with such name. Try again')
                    except et.ParseError:
                        print('Incorrect file .xml structure')
            else:
                print('Try again')
        return xml_file, path_for_remove

    def publishing(self):
        xml_file, path_for_remove = self.read_file()
        root = xml_file.getroot()
        insert_into_file = []
        for i in root.iter('block'):
            data = []
            if i.get('type') == 'News':
                try:
                    data.append('News:')
                    data.append(i.find('text').text + "\n")
                    data.append(i.find('city').text + ', ' + i.find('date').text + "\n")
                    insert_into_file.append(data)
                except AttributeError:
                    print("Important tag was absent for news")
                    insert_into_file = 'Empty'
                    break
                except TypeError:
                    print("Empty text in tag for news was found")
                    insert_into_file = 'Empty'
                    break
            elif i.get('type') == 'Private Ad':
                try:
                    data.append('News:')
                    data.append(i.find('text').text + "\n")
                    data.append(i.find('date').text + "\n")
                    insert_into_file.append(data)
                except AttributeError:
                    print("Important tag was absent for ad")
                    insert_into_file = 'Empty'
                    break
                except TypeError:
                    print("Empty text in tag for ad was found")
                    insert_into_file = 'Empty'
                    break
            elif i.get('type') == 'Question-divination':
                try:
                    data.append('News:')
                    data.append(i.find('question').text + "\n")
                    data.append(i.find('answer').text + "\n")
                    data.append(i.find('conclusion').text + "\n")
                    insert_into_file.append(data)
                except AttributeError:
                    print("Important tag was absent for divination")
                    insert_into_file = 'Empty'
                    break
                except TypeError:
                    print("Empty text in tag for divination was found")
                    insert_into_file = 'Empty'
                    break
            else:
                print('Some unknown type of records was found')
                insert_into_file = 'Empty'
                break

        return insert_into_file, path_for_remove


if __name__ == "__main__":
    # ask a user what data he wants to print and then call a class and insert the data into file using inserting method
    while True:
        print('What do you want to print?', '1 - News', '2 - Private Ad', '3 - Divination', '4 - Add data from another .txt file', '5 - Add data from .json file', '6 - Add data from .xml file', '7 - Nothing', sep='\n')
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
                print('Something went wrong with insertion data from the .txt file. Please fix the format of incoming file and try again\n')
            else:
                for d in data:
                    FromAnotherSource().formatting(d)
                    FromAnotherSource().inserting(d)
                print('The data from this file is published in Text.txt file')
                print(f'This file {path_for_remove} will be removed now\n')
                os.remove(path_for_remove)
        elif reply == '5':
            data, path_for_remove = FromJson().publishing()
            if data == 'Empty':
                print('Something went wrong with insertion data from the .json file. Please fix the format of incoming file and try again\n')
            else:
                for d in data:
                    FromJson().formatting(d)
                    FromJson().inserting(d)
                print('The data from this file is published in Text.txt file')
                print(f'This file {path_for_remove} will be removed now\n')
                os.remove(path_for_remove)
        elif reply == '6':
            data, path_for_remove = FromXml().publishing()
            if data == 'Empty':
                print('Something went wrong with insertion data from the .xml file. Please fix the format of incoming file and try again\n')
            else:
                for d in data:
                    FromXml().formatting(d)
                    FromXml().inserting(d)
                print('The data from this file is published in Text.txt file')
                print(f'This file {path_for_remove} will be removed now\n')
                os.remove(path_for_remove)
        elif reply == '7':
            print('You have updated the Text.txt file. The program is stopped.')
            CsvTasks().word_count()
            CsvTasks().letter_count()
            print('Word_count.csv and letter_count.csv files are updated')
            break
        else:
            print('Try again')
