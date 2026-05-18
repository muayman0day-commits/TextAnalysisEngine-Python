import re


def clean_text(text):
    """حذف العلامات ثم تحويل النص لصيغة موحدة."""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\u0600-\u06FF\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def split_words(text):
    """تقطيع النص إلى كلمات."""
    clean = clean_text(text)
    if not clean:
        return []
    return clean.split(" ")


def normalize_word(word):
    """تطبيع الكلمة للأحرف فقط."""
    return re.sub(r"[^a-zA-Z0-9\u0600-\u06FF]", "", word).lower()


def is_anagram(word1, word2):
    """تحقق إذا كانت الكلمتان متشابهتين (أناغرام)."""
    w1 = normalize_word(word1)
    w2 = normalize_word(word2)
    if not w1 or not w2:
        return False
    return sorted(w1) == sorted(w2)


def all_anagrams(words):
    """إيجاد جميع الأزواج المتشابهة في قائمة كلمات."""
    normalized = [(word, normalize_word(word)) for word in words if normalize_word(word)]
    results = []

    for i in range(len(normalized)):
        for j in range(i + 1, len(normalized)):
            if normalized[i][1] == normalized[j][1] and normalized[i][1]:
                results.append((normalized[i][0], normalized[j][0]))

    return results
