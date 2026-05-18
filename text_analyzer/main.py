from text_analyzer.text_utils import split_words, is_anagram, all_anagrams
from text_analyzer.statistics import count_words, most_common_words, unique_words
from text_analyzer.comparison import compare_texts


def run_example():
    text1 = "هذا مثال بسيط لتحليل النصوص. تحليل النص يساعد في معرفة الكلمات المتكررة."
    text2 = "هذا نص آخر، يمكننا مقارنته بالنص الأول، ونعرف الكلمات المشتركة والفريدة."

    print("=== تحليل النص الأول ===")
    print("عدد الكلمات:", count_words(text1))
    print("أكثر الكلمات تكراراً:", most_common_words(text1, top_n=3))
    print("الكلمات الفريدة:", unique_words(text1))
    print("أزواج الكلمات المتشابهة:", all_anagrams(split_words(text1)))
    print()

    print("=== مقارنة بين نصين ===")
    result = compare_texts(text1, text2)
    print("الكلمات المشتركة:", result["common_words"])
    print("الكلمات الموجودة فقط في النص الأول:", result["only_in_first"])
    print("الكلمات الموجودة فقط في النص الثاني:", result["only_in_second"])
    print("درجة التشابه:", result["similarity_score"])
    print()

    print("=== مثال أناغرام ===")
    print("هل 'listen' و 'silent' متشابهان؟", is_anagram("listen", "silent"))


if __name__ == "__main__":
    run_example()
