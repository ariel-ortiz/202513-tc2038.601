def gcd2(a: int, b: int) -> int:
    while True:
        r: int = a % b
        if r == 0:
            return b
        a, b = b, r


def gcd(a: int, b: int, *rest: int) -> int:
    result: int = gcd2(a, b)
    for n in rest:
        result = gcd2(result, n)
    return result


def are_coprimes(a: int, b: int) -> bool:
    return gcd2(a, b) == 1


def lcm(a: int, b: int) -> int:
    return a * b // gcd2(a, b)


if __name__ == '__main__':
    print(f'{gcd(20, 15) = }')
    print(f'{gcd(20, 150) = }')
    print(f'{gcd(20, 15, 35, 100, 50) = }')
    print(f'{are_coprimes(14, 25) = }')
    print(f'{are_coprimes(25, 15) = }')
    print(f'{lcm(10, 15) = }')
    print(f'{lcm(5, 10) = }')
    print(f'{lcm(2, 3) = }')
