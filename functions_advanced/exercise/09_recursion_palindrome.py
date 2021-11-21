# def palindrome(word: str, index: int):
#     new_word = word[::-1]
#
#     if word == new_word:
#         return f'{word} is a palindrome'
#     else:
#         return f'{word} is not a palindrome'


def palindrome(word: str, index=0):
    if index == len(word) // 2:
        return f'{word} is a palindrome'

    if not word[index] == word[(len(word) - index) - 1]:
        return f'{word} is not a palindrome'

    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
