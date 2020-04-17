import string
import train
import json
import cesar
import collections


# Уже кризис названий
def hack_cesar_from_string(input_string, model_filename):
    with open(model_filename) as f:
        right_frequency = json.load(f)

    # буду считать текст максимально реальный если средняя арифметическая модуля разниц частот минимальна
    median = 100
    right_key = 0
    for i in range(26):
        output_string = cesar.decode_caesar(i, input_string)
        new_freq = collections.Counter()
        train.get_frequency(new_freq, output_string)
        summary = 0
        for j in string.ascii_lowercase:
            summary += abs(right_frequency[j] - new_freq[j])
        summary /= 26
        if summary < median:
            median = summary
            right_key = i
    return right_key
