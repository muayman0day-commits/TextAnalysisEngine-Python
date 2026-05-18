from .text_utils import split_words


def compare_texts(text1, text2):
    """مقارنة نصين وإرجاع إحصائيات بسيطة."""
    words1 = set(split_words(text1))
    words2 = set(split_words(text2))

    common = words1.intersection(words2)
    only_in_first = words1 - words2
    only_in_second = words2 - words1

    total_words = len(words1) + len(words2)
    similarity = 0.0
    if total_words > 0:
        similarity = len(common) * 2 / total_words

    return {
        "common_words": sorted(common),
        "only_in_first": sorted(only_in_first),
        "only_in_second": sorted(only_in_second),
        "similarity_score": round(similarity, 3),
    }
