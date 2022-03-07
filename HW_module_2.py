# create a list of random number of dicts (from 2 to 10)

from random import randint, choice  # import necessary functions from random lib
from string import ascii_lowercase  # import necessary functions from string lib

list_of_dict = []  # create an empty list for our dictionaries
dict_numb = randint(2, 10)  # define random number (quantity) of future dictionaries we want to have in our list

for d in range(dict_numb):  # iterate through each dictionary as many times as the generated random showed
    random_dict = {}  # create an empty dictionary
    for i in range(randint(1, 27)):  # define random number (quantity) of key-value combinations we want to have in our random dictionary (from 1 to 27 because The English Alphabet consists of 26 letters)
        random_dict.update({choice(ascii_lowercase): randint(0, 100)})  # insert key which consists of random letter and insert value which consists of random number from 1 to 100
        # random_dict[choice(ascii_lowercase)] = randint(0, 100)  # alternative way to insert random key-value combination
    list_of_dict.append(random_dict)  # insert the created dictionary into our list

print('Initial list of dictionaries: ', list_of_dict)  # print initial list of dictionaries

#  get previously generated list of dicts and create one common dict:

distinct_keys = []  # create an empty list of distinct letters from all dictionaries in our list
duplicated_keys = []  # create an empty list of distinct letters which have duplicates (when the same letter occurs in at least two dictionaries)

for d in list_of_dict:  # go through each dictionary
    for key in d:  # go through each key in specified dictionary
        if key not in distinct_keys:  # check whether we already have the specified key in "distinct_keys" list
            distinct_keys.append(key)  # populate this list with each letter only once
        elif key not in duplicated_keys:  # if we have duplicated key we should populate...
            duplicated_keys.append(key)  # ... "duplicated_keys" list only once


distinct_keys.sort()  # sort "distinct_keys" list in alphabetical order
duplicated_keys.sort()  # sort "duplicated_keys" list in alphabetical order
print('Distinct_keys: ', distinct_keys)
print('Duplicated_keys: ', duplicated_keys)

one_common_dict = {}  # create an empty common dictionary

for key in distinct_keys:  # go through each letter from "distinct_keys" list
    if key in duplicated_keys:  # if this letter is in "duplicated_keys" list, then...
        max_value = 0  # let's define max value for each key (the default is zero)
        dict_number = 0  # define the number of the dictionary in the list
        for i, rand_dict in enumerate(list_of_dict):  # iterate over each dictionary and its index from the list using the function enumerate()
            if key in rand_dict and rand_dict[key] > max_value:  # check if the specified key is in the specified dictionary AND the key's value is bigger than max value
                max_value = rand_dict[key]  # then update max value
                dict_number = i + 1  # then update the number of the dictionary (started by 1)
        key_final = key + '_' + str(dict_number)  # create the key
        one_common_dict.setdefault(key_final, max_value)  # insert key and its max value in the one_common_dict
    if key not in duplicated_keys:  # if this letter is NOT in "duplicated_keys" list, then...
        for rand_dict in list_of_dict:  # iterate over each dictionary
            if key in rand_dict:  # check if the specified key is in the specified dictionary
                one_common_dict.setdefault(key, rand_dict[key])  # insert key and its value in the one_common_dict


print('Common dictionary: ', one_common_dict)  # show final sorted common dictionary
