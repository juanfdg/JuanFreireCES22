def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds


def merge(kvpair_list, ini, mid, fin):
    aux = []
    xi = ini
    yi = mid+1

    while True:
        if xi > mid:
            aux.extend(kvpair_list[yi:fin+1])
            break

        if yi > fin:
            aux.extend(kvpair_list[xi:mid+1])
            break

        if kvpair_list[xi][0] <= kvpair_list[yi][0]:
            aux.append(kvpair_list[xi])
            xi += 1

        else:
            aux.append(kvpair_list[yi])
            yi += 1

    for i in range(ini, fin+1):
        kvpair_list[i] = aux[i-ini]


def sort(kvpair_list, ini, fin):
    if ini < fin:
        mid = (ini+fin)//2
        sort(kvpair_list, ini, mid)
        sort(kvpair_list, mid+1, fin)
        merge(kvpair_list, ini, mid, fin)


def get_words_count(words_list):
    """ Return a list of tuples where the keys are each word in a list and the
    values are the number of times that a word occurs in the list"""
    count_dict = {}
    for word in words_list:
        count_dict[word] = count_dict.get(word, 0) + 1

    count = list(count_dict.items())
    sort(count, 0, len(count)-1)

    return count


def write_words_count_to_file(book, filename):
    wds = get_words_count(get_words_in_book(book))
    f = open(filename, 'w')
    f.write('Word              Count\n')
    f.write('=======================\n')
    for word in wds:
        f.writelines('{:17} {:>5}\n'.format(word[0], word[1]))


write_words_count_to_file('AlicesAdventuresInWonderland.txt', 'alice_words.txt')
