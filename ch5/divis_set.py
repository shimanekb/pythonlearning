#!/usr/bin/env python
def __compute_divisor_set(number: int):
    divisor_set = set()
    typed_number = int(number)
    for x in range(1, typed_number):
        if (typed_number % x == 0):
            divisor_set.update([x]);
    return divisor_set

def main():
    user_input = input("Enter an integer that is less than 100:\n")
    divisor_set = __compute_divisor_set(user_input)
    print(divisor_set)

if __name__ == '__main__':
    main()


