from collections import Counter
from .text_utils import split_words


def count_words(text):
    """عدد الكلمات في النص."""
    return len(split_words(text))


def most_common_words(text, top_n=5):
    """الكلمات الأكثر تكراراً في النص."""
    words = split_words(text)
    if not words:
        return []
    counter = Counter(words)
    return counter.most_common(top_n)


def unique_words(text):
    """إرجاع مجموعة الكلمات الفريدة في النص."""
    words = split_words(text)
    return list(dict.fromkeys(words))


def word_frequency(text):
    """عداد تردد الكلمات."""
    words = split_words(text)
    return dict(Counter(words))
