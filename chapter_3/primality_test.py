# 素数判定法
import math


def is_prime(n: int) -> bool:
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(100, 200):
        print(f'{i}: {is_prime(i)}')
