text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# create an empty list for normalized text
normalized_text = []
# split the text by tab into paragraphs (\t)
paragraphs = text.split('\t')
# go through each paragraph
for p in paragraphs:
    # split paragraph by words (by spaces)
    p_split = p.split(' ')
    # go through each word
    for n in range(len(p_split)):
        # in case when we face with index = 0 (the first word) OR when previous symbol was dot...
        if n == 0 or p_split[n-1][-1] == '.' or p_split[n-1][-1] == '!' or p_split[n-1][-1] == '?':
            # we should use the function capitalize()
            p_split[n] = p_split[n].capitalize()
        # if not, use lower() function
        else:
            p_split[n] = p_split[n].lower()
    # join updated paragraphs by spaces and insert them into "normalized_text" variable
    normalized_text.append(' '.join(p_split))

# join the paragraphs by tab into normalized text (\t)
normalized_text = '\t'.join(normalized_text)
# print(normalized_text)


# calculate number of whitespace characters in this text

# import lib for operations with regex
import re

# find all whitespaces, count them and print the result
whitespaces = re.findall('\s', normalized_text)
print('Number of whitespace characters: ', len(whitespaces))
print("---------------------------------------------------")

# create one more sentence with last words of each existing sentence and add it to the end of this paragraph.

# find all last words (the word before dot) and put them into list 'last_words'
last_words = re.findall('(\w*?)[.|!|?]', normalized_text)
# print('last_words', last_words)
# add hardcoded value before the first word and capitalize the first word
for i in range(len(last_words) - 1):
    if i == 0:
        last_words[i] = last_words[i].capitalize()
    else:
        last_words[i] = last_words[i].lower()
last_words[0] = 'HARDCODED_VALUE_FOR_SPLIT' + last_words[0]
# create new sentence by joining elements
new_sentence = ' '.join(last_words)
new_sentence = new_sentence + '.'
# split "normalized_text" by paragraphs to make it easier to insert new sentence
normalized_text_split = normalized_text.split('\n\n')
# insert new sentence to the end of the second paragraph
normalized_text_split.insert(2, new_sentence)
# join paragraphs by double "\n" and insert them into "normalized_text_upd" variable
normalized_text_upd = '\n\n'.join(normalized_text_split)
# in order to put new sentence to the end of the second paragraph without creating new paragraph, we should perform such replacement:
normalized_text_upd = normalized_text_upd.split('\n\nHARDCODED_VALUE_FOR_SPLIT')
normalized_text_upd_2 = ' '.join(normalized_text_upd)


# fix “iz” with correct “is”, but only when it iz a mistake and add space before quotes where necessary
# substitute incorrect pattern by correct one
normalized_text_upd_3 = re.sub(' iz ', ' is ', normalized_text_upd_2)

# substitute quotes as space+quotes
normalized_text_upd_4 = re.sub('“', ' “', normalized_text_upd_3)
# substitute all double spaces by single one
normalized_text_upd_4 = re.sub('  ', ' ', normalized_text_upd_4)
print(normalized_text_upd_4)

