import string
import train
import json
import collections
import alphabet


def hack_cesar_from_string(input_string, model_filename):
    with open(model_filename) as f:
        right_frequency = json.load(f)

    # буду считать текст максимально реальный если средняя арифметическая модуля разниц частот минимальна
    median = 100
    right_key = 0
    ordinary_frequency = collections.Counter()
    train.get_frequency(ordinary_frequency, input_string)
    for i in range(alphabet.size):
        new_freq = collections.Counter()
        for j in string.ascii_lowercase:
            new_freq[j] = ordinary_frequency[alphabet.lowercase_dict[(alphabet.lowercase[j] + i) % alphabet.size]]
        summary = 0
        for j in string.ascii_lowercase:
            summary += abs(right_frequency[j] - new_freq[j])
        summary /= alphabet.size
        if summary < median:
            median = summary
            right_key = i
    return right_key
