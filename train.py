# Train
import alphabet
import string
import json
from _collections import defaultdict


def get_frequency(frequency, input_string):
    letter_count = 0
    for it in input_string:

        if it in alphabet.lowercase:
            frequency[it] += 1
            letter_count += 1
        elif it in alphabet.uppercase:
            frequency[alphabet.lowercase_dict[alphabet.uppercase[it]]] += 1
            letter_count += 1
    for i in string.ascii_lowercase:
        frequency[i] /= letter_count


def train(input_string, filename):
    freq = defaultdict(int)
    get_frequency(freq, input_string)
    with open(filename, 'w') as tmp:
        json.dump(freq, tmp)
