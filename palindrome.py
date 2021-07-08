# Palindrome verification using slices
def palindrome(word):
    word = word.replace(' ','')
    word = word.lower()
    word_inverted = word[::-1]
    if word == word_inverted:
        return True
    else:
        return False


def run():
    word = input('Input a word or phrase: ')
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print('It is a palindrome')
    else:
        print('It is not a plaindrome')


# Entry Point
if __name__ == '__main__':
    run()
