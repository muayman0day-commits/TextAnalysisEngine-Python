from text_analyzer.text_utils import split_words, is_anagram, all_anagrams
from text_analyzer.statistics import count_words, most_common_words, unique_words, word_frequency
from text_analyzer.comparison import compare_texts


def test_split_words():
    assert split_words("Hello world!") == ["hello", "world"]
    assert split_words("") == []


def test_is_anagram():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("hello", "world") is False


def test_all_anagrams():
    pairs = all_anagrams(["listen", "silent", "enlist", "hello"])
    assert ("listen", "silent") in pairs
    assert ("listen", "enlist") in pairs


def test_statistics():
    text = "apple apple orange"
    assert count_words(text) == 3
    assert most_common_words(text, 2) == [("apple", 2), ("orange", 1)]
    assert unique_words(text) == ["apple", "orange"]
    assert word_frequency(text)["apple"] == 2


def test_compare_texts():
    result = compare_texts("apple orange", "orange banana")
    assert result["common_words"] == ["orange"]
    assert result["only_in_first"] == ["apple"]
    assert result["only_in_second"] == ["banana"]


def run_tests():
    test_split_words()
    test_is_anagram()
    test_all_anagrams()
    test_statistics()
    test_compare_texts()
    print("جميع الاختبارات نجحت.")


if __name__ == "__main__":
    run_tests()
