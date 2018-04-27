# Module created for exercise 12.11.3 of the book
# How to Think Like a Computer Scientist


def cleanword(string):
    new_string = ''
    for c in string:
        if c.isalpha():
            new_string += c

    return new_string


def has_dashdash(string):
    return "--" in string


def extract_words(string):
    list = ['']
    length = len(string)
    word_count = 0

    for i in range(length):
        if not string[i].isalpha():
            continue

        list[word_count] += string[i].lower()

        if i < length-1 and not string[i+1].isalpha():
            word_count += 1
            list.append('')

    if list[-1] == '':
        list.remove(list[-1])

    for i in range(len(list)):
        list[i] = cleanword(list[i])

    return list

def wordcount(string, list):
    count = 0

    for word in list:
        if word == string:
            count += 1

    return count

def wordset(words):
    list = ['']

    for word in words:
        i = 0
        while i < len(list) and word > list[i]:
            i += 1

        if i < len(list) and word == list[i]:
            continue

        list.insert(i, word)

    list.remove(list[0])
    return list

def longestword(words):
    longestword = ''

    for word in words:
        if len(word) > len(longestword):
            longestword = word

    return len(longestword)
