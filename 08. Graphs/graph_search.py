from typing import Iterator
from collections import deque


type Graph = dict[str, list[str]]


def depth_first_search(
        start: str,
        graph: Graph) -> Iterator[str]:
    stack: deque[str] = deque()
    visited: set[str] = set()
    stack.append(start)
    while stack:
        current: str = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(graph[current][::-1])
            yield current


if __name__ == "__main__":
    g: Graph = {
        'A': ['B', 'C', 'F'],
        'B': ['A', 'D'],
        'C': ['A', 'E', 'F'],
        'D': ['B'],
        'E': ['C', 'F'],
        'F': ['A', 'C', 'E', 'G'],
        'G': ['F']
    }
    print(list(depth_first_search('A', g)))
    print(list(depth_first_search('G', g)))
    print(list(depth_first_search('E', g)))
    start = 'A'
    end = 'D'
    for v in depth_first_search(start, g):
        print(v)
        if v == end:
            break
