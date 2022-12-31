import math


def convert_decimal_to_binary():
    print('Please enter a number:', end=' ')
    n: int = int(input())
    ans: str = ''

    while n >= 1:
        if n % 2 == 0:
            ans = '0' + ans
        elif n % 2 == 1:
            ans = '1' + ans
        n = math.floor(n / 2)

    print(f'answer: {ans}')


if __name__ == '__main__':
    convert_decimal_to_binary()
