#Train
import alphabet
import string
import json
import collections


def set_initial_values(frequency):
    for i in string.ascii_lowercase:
        frequency[i] = 0


def get_frequency(frequency, input_string):
    set_initial_values(frequency)
    word_count = 0
    for it in input_string:

        if it in alphabet.lowercase:
            frequency[it] += 1
            word_count += 1
        elif it in alphabet.uppercase:
            frequency[alphabet.lowercase[alphabet.uppercase[it]]] += 1
            word_count += 1
    for i in string.ascii_lowercase:
        frequency[i] /= word_count


def train(input_string, filename):
    freq = collections.Counter()
    get_frequency(freq, input_string)
    with open(filename, 'w') as tmp:
        json.dump(freq, tmp)
