#!/usr/bin/env python

SUB_STRING = 'on'

def main():
    user_input = input('Enter a word:\n')
    print('Checking if the substring "%s" is in "%s"' % (SUB_STRING, user_input))
    print('Result: %r' % (SUB_STRING in user_input))

if __name__ == '__main__':
    main()
