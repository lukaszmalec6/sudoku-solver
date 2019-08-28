#   1   2   3   |  4   5   6   |  7   8   9
#   A1  A2  A3  |  A4  A5  A6  |  A7  A8  A9
#   B1  B2  B3  |  B4  B5  B6  |  B7  B8  B9
#   C1  C2  C3  |  C4  C5  C6  |  C7  C8  C9
#   ------------+--------------+------------
#   D1  D2  D3  |  D4  D5  D6  |  D7  D8  D9
#   E1  E2  E3  |  E4  E5  E6  |  E7  E8  E9
#   F1  F2  F3  |  F4  F5  F6  |  F7  F8  F9
#   ------------+--------------+------------
#   G1  G2  G3  |  G4  G5  G6  |  G7  G8  G9
#   H1  H2  H3  |  H4  H5  H6  |  H7  H8  H9
#   I1  I2  I3  |  I4  I5  I6  |  I7  I8  I9


def display(values, cells, rows, cols):
    """Display these values as a 2-D grid."""
    width = 1 + max(len(values[cell]) for cell in cells)
    line = '+'.join(['-'*(width * 3)] * 3)
    for row in rows:
        print(''.join(values[row + col].center(width) +
                      ('|' if col in '36' else '') for col in cols))
        if row in 'CF':
            print(line)
    print('\n')


def get_initial_grid(input, cols, rows):
    """Returns grid for sudoku puzzles"""
    return dict((row + col, {}) for row in rows for col in cols)


def parse_input(input_data, grid):
    """Returns grid with initial values"""
    # eg input 003020600900305001001806400008102900700000008006708200002609500800203009005010300
    result = {}
    grid_keys = list(grid.keys())
    for i in range(len(grid_keys)):
        value = input_data[i]
        if (value == '0'):
            value = '123456789'
        result[grid_keys[i]] = value
    return result


def cross(a, b):
    """Returns A+B for elements in A and elements in B."""
    return [x + y for x in a for y in b]


def get_cell_grid(cells, units_list):
    """Returns dictionary where cell index is key, and indexes in unit
    for cell are values eg A1: {[...], [...], [...]]."""
    result = {}
    for cell in cells:
        for unit in units_list:
            if cell in unit:
                if cell not in result.keys():
                    result[cell] = []
                result[cell].append(unit)
    return result


def get_cell_grid_indexes(cells, cell_grid):
    """Returns dictionary where cell index is key, and unique indexes for cells in
    units are values eg A1: {'A2', 'B2', 'B3'}."""
    result = {}
    for cell in cells:
        result[cell] = (set(sum(cell_grid[cell], [])) - set([cell]))
    return result


def eliminate(cell_index, grid, cell_grid_indexes):
    if len(grid[cell_index]) == 1:
        return grid[cell_index]
    current_grid_values = ''
    for cg in cell_grid_indexes:
        val = grid[cg]
        if len(val) == 1:
            current_grid_values += val
    cell_grid_values = grid[cell_index]
    result = ''
    for value in cell_grid_values:
        if value not in current_grid_values:
            result += value
    return result
