from __future__ import annotations
from typing import cast
from collections.abc import Iterable, Iterator


class _Node[N]:

    info: N | None
    next: _Node[N]
    prev: _Node[N]

    # Complexity: O(1)
    def __init__(self, value: N | None = None) -> None:
        self.info = value
        self.next = self
        self.prev = self


class OrderedSet[T]:

    __sentinel: _Node[T]
    __count: int

    # Complexity: O(N^2)
    def __init__(self, values: Iterable[T] = []) -> None:
        self.__sentinel = _Node()
        self.__count = 0
        for elem in values:
            self.add(elem)

    # Complexity: O(1)
    def __len__(self) -> int:
        return self.__count

    # Complexity: O(N)
    def __repr__(self) -> str:
        return f"OrderedSet({list(self) if self else ''})"

    # Complexity: O(N)
    def add(self, value: T) -> None:
        if value in self:
            return
        self.__count += 1
        new_node: _Node[T] = _Node(value)
        new_node.prev = self.__sentinel.prev
        new_node.next = self.__sentinel
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    # Complexity: O(N)
    def __iter__(self) -> Iterator[T]:
        current: _Node[T] = self.__sentinel.next
        while current is not self.__sentinel:
            yield cast(T, current.info)
            current = current.next

    # Complexity: O(N)
    def __contains__(self, value: T) -> bool:
        for elem in self:
            if elem == value:
                return True
        return False

    # Complexity: O(N*M) where N = len(self) and M = len(other)
    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        if not isinstance(other, OrderedSet):
            return False
        if len(self) != len(other):  # type: ignore
            return False
        for elem in self:
            if elem not in other:
                return False
        return True

    # Complexity: O(N*M) where N = len(self) and M = len(other)
    def __le__(self, other: OrderedSet[T]) -> bool:
        if self is other:
            return True
        if len(self) > len(other):
            return False
        for elem in self:
            if elem not in other:
                return False
        return True

    # Complexity: O(N*M) where N = len(self) and M = len(other)
    def __and__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem in other:
                result.add(elem)
        return result

    # Complexity: O(N)
    def discard(self, value: T) -> None:
        current: _Node[T] = self.__sentinel.next
        while current is not self.__sentinel:
            if current.info == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.__count -= 1
                return
            current = current.next


if __name__ == '__main__':
    s1: OrderedSet[int] = OrderedSet([4, 8, 15, 16, 23, 42])
    s2: OrderedSet[int] = OrderedSet(s1)
    s3: OrderedSet[int] = s1
    print(f'{s1 = }')
    print(f'{s2 = }')
    print(f'{s1 == s2 = }')
    print(f'{s1 is s2 = }')
    print(f'{s1 is s3 = }')
    s4: OrderedSet[int] = OrderedSet([8, 42])
    print(f'{s4 <= s1 = }')
    print(f'{s1 <= s4 = }')
    print(f'{s4 <= s4 = }')
    s5: OrderedSet[int] = OrderedSet()
    print(f'{s5 <= s1 = }')
    print(f'{s4 <= s1 = }')
    print(f'{s1 <= s5 = }')
    print(f'{s1 <= s1 = }')
    print(f'{s4 = }')
    s4.discard(42)
    print(f'{s4 = }')
    s4.discard(42)
    print(f'{s4 = }')
    print(f'{len(s4) = }')
