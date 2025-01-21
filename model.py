class Cell:
    def __init__(self, coord: tuple[int]) -> None:
        self.activated = False
        self.alive = False
        self.coord = coord

    def __str__(self) -> str:
        return "#" if self.alive else ("~" if self.activated else " ")

    def __repr__(self) -> str:
        return "#" if self.alive else ("~" if self.activated else " ")


class Grid:
    def __init__(self, iter: int, rule: list[bool]) -> None:
        self.cells = [
            [Cell((x, y)) for x in range(iter * 2 + 1)] for y in range(iter * 2 + 1)
        ]
        self.rule = rule

    def __str__(self) -> str:
        return str(
            f"\n{'-'*(3*len(self.cells)+len(self.cells)-1)}\n".join(
                ["|".join([str(n).center(3, " ") for n in row]) for row in self.cells]
            )
        )


def test_grid():
    grid = Grid(5, [0, 0, 0, 1, 1, 1, 1, 0, 1, 1])
    print(grid)


if __name__ == "__main__":

    test_grid()
