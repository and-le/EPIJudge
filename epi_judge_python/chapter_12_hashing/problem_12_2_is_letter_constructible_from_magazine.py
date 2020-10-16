import collections
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    return not (collections.Counter(letter_text) - collections.Counter(magazine_text))


def main():
    assert is_letter_constructible_from_magazine("abc", "aabbcc")
    assert is_letter_constructible_from_magazine("abc", "abc")
    assert not is_letter_constructible_from_magazine("abcd", "abc")
    assert not is_letter_constructible_from_magazine("aabc", "abc")



    print("All assertions correct")



if __name__ == "__main__":
    main()
