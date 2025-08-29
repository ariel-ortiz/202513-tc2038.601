
# O(1)
def is_even(n: int) -> bool:
    return (n & 1) == 0

# O(1)
def turn_uneven(n: int) -> int:
    return n | 1

# O(log N)
def count_bits(n: int) -> int:
    count: int = 0
    while n:
        count += (n & 1)
        n >>= 1
    return count


if __name__ == '__main__':
    print(f'{is_even(4) = }')
    print(f'{is_even(13) = }')
    print(f'{is_even(666) = }')
    print(f'{is_even(665) = }')
    print(f'{turn_uneven(5) = }')
    print(f'{turn_uneven(10) = }')
    print(f'{count_bits(0) = }')
    print(f'{count_bits(1) = }')
    print(f'{count_bits(27) = }')
    print(f'{count_bits(1024) = }')
    print(f'{count_bits(1023) = }')
