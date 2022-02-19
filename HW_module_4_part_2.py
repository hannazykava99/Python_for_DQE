text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# define functions with parameters


def capitalize(index, word):
    if index == 0 or word[index-1][-1] in ('.', '!', '?'):
        word[index] = word[index].capitalize()
    else:
        word[index] = word[index].lower()


def letter_case_normalization(txt):
    # create an empty list for normalized text
    normalized_text = []
    # split the text by tab into paragraphs (\t)
    paragraphs = txt.split('\t')
    # go through each paragraph
    for p in paragraphs:
        # split paragraph by words (by spaces)
        p_split = p.split(' ')
        # go through each word
        for n in range(len(p_split)):
            # use capitalize function
            capitalize(n, p_split)
        # join updated paragraphs by spaces and insert them into "normalized_text" variable
        normalized_text.append(' '.join(p_split))
    # join the paragraphs by tab into normalized text (\t)
    final_text = '\t'.join(normalized_text)
    return final_text


# call the function with the defined parameter
normalized_text = letter_case_normalization(text)

# calculate number of whitespace characters in this text
def sum_whitespaces(txt):
    # import lib for operations with regex
    import re
    # find all whitespaces, count them and print the result
    whitespaces = re.findall('\s', txt)
    len_whitespaces = len(whitespaces)
    return len_whitespaces

number_whitespaces = sum_whitespaces(text)

# print the result
print('Number of whitespace characters: ', number_whitespaces)

print("---------------------------------------------------")
print()


# create one more sentence with last words of each existing sentence and add it to the end of this paragraph.
def new_sentence(txt):
    import re
    # find all last words (the word before dot) and put them into list 'last_words'
    last_words = re.findall('(\w*?)[.|!|?]', txt)
    # print('last_words', last_words)
    # capitalize the first word and make the other in lower case
    for i in range(len(last_words)-1):
        capitalize(i, last_words)
    # create new sentence by joining elements
    new_sentence = ' '.join(last_words)
    new_sentence = new_sentence + '.'
    return new_sentence

new_sentence = new_sentence(normalized_text)

def add_sent_to_second_paragraph(sent):
    # split "normalized_text" by paragraphs to make it easier to insert new sentence
    normalized_text_split = normalized_text.split('\n\n')
    # insert new sentence to the end of the paragraph by template
    x = 'not found'
    # go through each paragraph to find the index of the required paragraph
    # set this index by default (insert sentence in the end of the paragraph)
    p_index = -1
    for ind, p in enumerate(normalized_text_split):
        # split by words
        p = p.split(' ')
        if x == 'not found':
            # go through each word
            for i in range(len(p)):
                # let's find the paragraph by template
                if p[i] == 'the' and p[i+1] == 'end' and p[i+2] == 'of' and p[i+3] == 'this' and p[i+4] == 'paragraph.':
                    # when we find, we need to break the loop
                    p_index = ind
                    x = 'found'
                    break
    normalized_text_split[p_index] = normalized_text_split[p_index] + ' ' + sent
    # join paragraphs by double "\n" and insert them into "normalized_text_upd_2" variable
    normalized_text_upd_2 = '\n\n'.join(normalized_text_split)
    return normalized_text_upd_2


normalized_text_with_sentence = add_sent_to_second_paragraph(new_sentence)


def correct_iz_to_is(txt):
    import re
    # fix “iz” with correct “is”, but only when it iz a mistake and add space before quotes where necessary
    # substitute incorrect pattern by correct one
    normalized_text_upd_3 = re.sub(' iz ', ' is ', txt)
    return normalized_text_upd_3

corrected_text = correct_iz_to_is(normalized_text_with_sentence)

def add_space_before_quote(a):
    import re
    # substitute quotes as space+quotes
    normalized_text_upd_4 = re.sub('“', ' “', a)
    # substitute all double spaces by single one
    normalized_text_upd_4 = re.sub('  ', ' ', normalized_text_upd_4)
    return normalized_text_upd_4

final_text = add_space_before_quote(corrected_text)
print(final_text)
