from pprint import pprint

# List comprehension
print([2 ** i for i in range(5)])

# List comprehension
print([c.upper() for c in 'Hello, World!' if c not in ' oe'])

# List comprehension with cartesian product
print([(x, y) for x in 'abc' for y in [1, 2]])

# List comprehension. Pythagorean Triples.
pprint([(a, b, c) for a in range(1, 101)
                  for b in range(1, 101)
                  for c in range(1, 101)
                  if a <= b <= c and a ** 2 + b ** 2 == c ** 2])

# Set comprehension
print({c.upper() for c in 'Hello, World!'})

# Dicitionay comprehension
print({i: 2 ** i for i in range(5)})

# Generator comprehension
g = (2 ** i for i in range(1_000_000_000))
print(next(g))
print(next(g))
print(next(g))
for x in g:
    print(x)
    if x > 1_000:
        break
