#!/usr/bin/env python

def is_palindrome(word):
    result = False 
    if (word[::-1] == word):
        result = True
    return result

def main():
    user_input = input('Enter a word:\n')
    output = (
            'It is %r that %s is a palindrome.' % 
            (is_palindrome(user_input), user_input)
            )
    print(output)

if __name__ == '__main__':
    main()
