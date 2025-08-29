a: int = 5    # 0b0101
b: int = 9    # 0b1001
c: int = 15   # 0b1111

print(f'{bin(a) = }')
print(f'{oct(b) = }')
print(f'{hex(c) = }')

s: str = '1010'
print(f'{int(s, 10) = }')
print(f'{int(s, 2) = }')
print(f'{int(s, 8) = }')
print(f'{int(s, 16) = }')
print(f'{int(s, 36) = }')

print(f'{a & b = }')
print(f'{a & c = }')
print(f'{b & c = }')

print(f'{a | b = }')
print(f'{a | c = }')
print(f'{b | c = }')

print(f'{a ^ b = }')
print(f'{a ^ c = }')
print(f'{b ^ c = }')

print(f'{~a = }')
print(f'{~b = }')
print(f'{~c = }')

print(f'{a << 3 = }')
print(f'{b << 2 = }')
print(f'{c << 1 = }')

print(f'{a >> 3 = }')
print(f'{b >> 2 = }')
print(f'{c >> 1 = }')
