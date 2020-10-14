import collections
def can_form_palindrome(s):
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


def main():
    assert can_form_palindrome("edified") == True
    assert can_form_palindrome("levxel") == False
    assert can_form_palindrome("toot") == True
    print("All assertions correct")



if __name__ == "__main__":
    main()
