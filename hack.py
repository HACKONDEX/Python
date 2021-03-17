import string
import train
import collections
import alphabet


def hack_caesar_from_string(input_string, right_frequency):
    # буду считать текст максимально реальный если средняя арифметическая модуля разниц частот минимальна
    average_arithmetical = float("inf")
    right_key = 0
    ordinary_frequency = collections.Counter()
    train.get_frequency(ordinary_frequency, input_string)
    for i in range(alphabet.size):
        summary = 0
        for j in string.ascii_lowercase:
            summary += abs(right_frequency[j] - ordinary_frequency[alphabet.lowercase_dict[(alphabet.lowercase[j] + i) % alphabet.size]])
        if summary < average_arithmetical:
            average_arithmetical = summary
            right_key = i
    return right_key
