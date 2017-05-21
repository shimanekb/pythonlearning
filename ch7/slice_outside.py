#!/usr/bin/env python

def __trim_first_last_char(text):
    trimmed_text = ''
    if (len(text) > 2):
        trimmed_text = text[1:-1]
    return trimmed_text

def main():
    user_input = input('Enter a word:\n')
    print('Result: %s' % (__trim_first_last_char(user_input)))

if __name__ == '__main__':
    main()
