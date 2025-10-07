from typing import NamedTuple
from csp import Constraint, CSP


type Grid = list[list[int]]


class GridLocation(NamedTuple):
    row: int
    column: int


def is_magic_square(square: Grid) -> bool:
    ((a, b, c),
     (d, e, f),
     (g, h, i)) = square
    return (   (a + b + c) # Rows
            == (d + e + f)
            == (g + h + i)
            == (a + d + g) # Columns
            == (b + e + h)
            == (c + f + i)
            == (a + e + i) # Diagonals
            == (c + e + g))


def convert_to_grid(assignment: dict[int, GridLocation]) -> Grid:
    square: Grid = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
    for var, (row, column) in assignment.items():
        square[row][column] = var
    return square


class MagicSquareConstraint(Constraint[int, GridLocation]):

    def __init__(self, variables: list[int]) -> None:
        super().__init__(variables)
        self.variables: list[int] = variables

    def satisfied(self, assignment: dict[int, GridLocation]) -> bool:
        if len(assignment) != len(set(assignment.values())):
            return False
        if len(assignment) < 9:
            return True
        return is_magic_square(convert_to_grid(assignment))
    

def solve_magic_square() -> None:
    variables: list[int] = list(range(1, 10))
    all_grid_locations: list[GridLocation] = [GridLocation(r, c) 
                                              for r in range(3) 
                                              for c in range(3)]
    domains: dict[int, list[GridLocation]] = { 
        var: all_grid_locations for var in variables
    }
    csp: CSP[int, GridLocation] = CSP(variables, domains)
    csp.add_constraint(MagicSquareConstraint(variables))
    solution: dict[int, GridLocation] | None = csp.backtracking_search()
    if solution:
        print(convert_to_grid(solution))
    else:
        print("No solution found :(")


if __name__ == "__main__":
    # a: GridLocation = GridLocation(1, 1)
    # b: GridLocation = GridLocation(1, 1)
    # print(a, b)
    # print(a == b)
    # print(a.row)
    # print(a[0])
    # r, c = a
    # print(r, c)
    # print(hash(a))
    # print(hash(b))
    # print(is_magic_square([[4, 3, 8], [9, 5, 1], [2, 7, 6]]))
    # print(is_magic_square([[3, 4, 8], [9, 5, 1], [2, 7, 6]]))
    # print(convert_to_grid({
    #     1: GridLocation(1, 2),
    #     2: GridLocation(2, 0),
    #     3: GridLocation(0, 1),
    #     4: GridLocation(0, 0),
    #     5: GridLocation(1, 1),
    #     6: GridLocation(2, 2),
    #     7: GridLocation(2, 1),
    #     8: GridLocation(0, 2),
    #     9: GridLocation(1, 0),
    # }))
    solve_magic_square()