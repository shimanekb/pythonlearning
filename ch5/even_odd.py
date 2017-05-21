#!/usr/bin/env python

def __even_odd_update(number):
    int_number = int(number)
    if (int_number % 2 == 0):
        int_number *= 2
    else:
        int_number //= 2
    return int_number

def main():
    user_input = input("Enter an integer:\n")
    print(__even_odd_update(user_input))

if __name__ == "__main__":
    main()
