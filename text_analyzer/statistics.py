from collections import Counter
from .text_utils import split_words


def count_words(text):
    return len(split_words(text))


def most_common_words(text, top_n=5):
    words = split_words(text)
    if not words:
        return []
    counter = Counter(words)
    return counter.most_common(top_n)


def unique_words(text):
    words = split_words(text)
    return list(dict.fromkeys(words))


def word_frequency(text):
    words = split_words(text)
    return dict(Counter(words))
