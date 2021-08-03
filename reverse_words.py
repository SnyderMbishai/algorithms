"""
Given an input string, reverse the string word by word.
"""

def reverse_words(string):
    string_list = string.split(" ")
    if len(string_list) <= 1:
        return string
    reversed_words = string_list[::-1]
    return ' '.join(reversed_words)

if __name__=='__main__':
    print(reverse_words("one"))
    print(reverse_words("one two"))
    print(reverse_words(""))