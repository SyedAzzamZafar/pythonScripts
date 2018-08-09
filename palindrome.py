"""This is a program to check whether a word is a palindrome or not.
 The program returns True
 in case the word being a palindrome and False otherwise."""

def is_palindrome(word):
    if len(word)==1:
        return True

    elif len(word)==2 and word[0]==word[-1]:
        return True

    elif word[0]==word[-1]:
        return is_palindrome(word[1:-1])


    else:
        return False


print(is_palindrome(input('Enter word\n')))
