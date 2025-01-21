from copy import deepcopy
from typing import Union

# local
from model import Grid


def neighbors(grid: Grid, coord: tuple[int]) -> list[Union[tuple[int], bool]]:
    """return the index of [up, right, down, left] neighbor's coord (x, y)

    if one neighbor does not exist, return False instead"""
    n_coords = []
    for x, y in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        n_coord = (coord[0] + x, coord[1] + y)
        if (
            0 <= n_coord[0] <= len(grid.cells) - 1
            and 0 <= n_coord[1] <= len(grid.cells) - 1
        ):
            n_coords.append(n_coord)
        else:
            n_coords.append(False)

    return n_coords


def act_cells(grid: Grid) -> Grid:
    """activate all activated cells' neighbor"""
    new_grid = deepcopy(grid)
    for row in grid.cells:
        for cell in row:
            if cell.activated:
                for coord in neighbors(grid, cell.coord):
                    if coord:
                        new_grid.cells[coord[1]][coord[0]].activated = True
    return new_grid


def get_rule(rule: int) -> list[bool]:
    bin_rule = bin(rule)[2:]
    bin_rule = (10 - len(bin_rule)) * "0" + bin_rule
    rule_list: list[bool] = []
    for n in bin_rule:
        if int(n):
            rule_list.append(True)
        else:
            rule_list.append(False)
    return rule_list


def search_alive(grid: Grid, coord: tuple[int]) -> int:
    num = 0

    n_coords = neighbors(grid, coord)
    for n_coord in n_coords:
        if n_coord:
            if grid.cells[n_coord[1]][n_coord[0]].alive:
                num += 1
    return num


def init(iter: int, rule: int) -> Grid:

    grid = Grid(iter, get_rule(rule))
    grid.cells[iter][iter].activated = True
    grid = act_cells(grid)
    grid.cells[iter][iter].alive = True

    return grid


def next_iter(grid: Grid) -> Grid:
    new_grid = deepcopy(grid)
    new_grid = act_cells(new_grid)
    for row in grid.cells:
        for cell in row:
            if cell.activated:
                alive_num = search_alive(grid, cell.coord)

                new_grid.cells[cell.coord[1]][cell.coord[0]].alive = grid.rule[
                    8 - (alive_num * 2) + (not cell.alive)
                ]
    return new_grid


if __name__ == "__main__":

    print("\n\nget_rule() test...")
    print(get_rule(999))

    print("\n\nact_cells() test...")
    test_grid = Grid(3, get_rule(999))
    test_grid.cells[3][3].activated = True
    print("before:")
    print(test_grid)
    print("after:")
    test_grid = act_cells(test_grid)
    print(test_grid)

    print("\n\nsearch_alive() test...")
    test_grid.cells[3][3].alive = True
    print(test_grid)
    print(f"test on coord (3,3): {search_alive(test_grid,(3,3))}")
    print(f"test on coord (2,3): {search_alive(test_grid,(2,3))}")
    print("\n\ninit() test...")
    test_grid = init(3, 999)
    print(test_grid)

    print("\n\nnext_iter() test...")
    test_grid = next_iter(test_grid)
    print(test_grid)
