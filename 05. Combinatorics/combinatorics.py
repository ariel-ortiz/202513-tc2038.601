from pprint import pprint


def nicely_sorted[T](s: list[list[T]]) -> list[list[T]]:

    def size_and_content(value: list[T]) -> tuple[int, list[T]]:
        return (len(value), value)

    return sorted(s, key=size_and_content)


# Complexity: O(2^N)
def power_set[T](s: list[T]) -> list[list[T]]:
    if not s:
        return [[]]
    temp: list[list[T]] = power_set(s[:-1])
    return temp + [e + [s[-1]] for e in temp]


if __name__ == '__main__':
    pprint(power_set([])) # type: ignore
    pprint(power_set(['a']))
    pprint(power_set(['a', 'b']))
    pprint(nicely_sorted(power_set(['a', 'b', 'c'])))
    pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd'])))
    pprint(nicely_sorted(power_set(['a', 'b', 'c', 'd', 'e'])))
