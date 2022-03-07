# create list of 100 random numbers from 0 to 1000
from random import randint  # import randint() function from "random" module which returns a random number between the given range

n = 100  # create a variable (how many elements we want to have in the list)
array = list()  # create an empty list
for i in range(n):  # iterate through each element from the specified range
    array.append(randint(0, 1000))  # insert new random element in the list 100 times

# sort list from min to max (without using sort())
for run in range(len(array) - 1):  # make as many rounds in the loop as there are elements except for the last one (the most minimal element)
    for i in range(len(array) - 1 - run):  # go through each element except the last one (because the last element doesn't have right neighbor). We also may optimize the code by subtracting the number of runs
        if array[i] > array[i + 1]:  # we need to compare neighboring elements and if the left element is greater than the right one...
            array[i], array[i + 1] = array[i + 1], array[i]  # ...we will swap them
# print(array)

# calculate average for even and odd numbers and print them
even_summa = 0  # create a variable for the sum of even numbers
odd_summa = 0  # create a variable for the sum of odd numbers
even_count = 0  # create a variable for the quantity of even numbers
odd_count = 0  # create a variable for the quantity of odd numbers

for i in range(len(array)):  # we need to check each element in the list
    if array[i] % 2 == 0:  # if we divide an element by two and receive an empty remainder from the division, it means that we face with an even number
        even_summa += array[i]  # add an even number in variable for the sum of even numbers
        even_count += 1  # increase the quantity of even numbers by one
    else:  # if we divide the element by two and don't receive an empty remainder
        odd_summa += array[i]   # add an odd number in variable for the sum of odd numbers
        odd_count += 1  # increase the quantity of odd numbers by one

try:  # let's check if we don't divide by zero
    even_avg = even_summa / even_count  # then calculate the average for even numbers
    print("Average for even numbers from the array: ", even_avg)  # print the result for even numbers
except ZeroDivisionError:  # if we divide by zero
    print("It's impossible to calculate average for even numbers because we can't delete by zero")  # we should print the text with explanation

try:  # let's check if we don't divide by zero
    odd_avg = odd_summa / odd_count  # then calculate the average for odd numbers
    print("Average for odd numbers from the array: ", odd_avg)  # print the result for odd numbers
except ZeroDivisionError:  # if we divide by zero
    print("It's impossible to calculate average for odd numbers because we can't delete by zero")  # we should print the text with explanation
