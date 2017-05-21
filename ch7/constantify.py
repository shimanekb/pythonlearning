#!/usr/bin/env python

def __constantify(text):
    return text.upper().replace(' ', '_')

def main():
    user_input = input('Enter in some text:\n')
    print(__constantify(user_input))

if __name__ == '__main__':
    main()
