from lib import (
    cross,
    get_cell_grid,
    get_cell_grid_indexes,
    get_initial_grid,
    parse_input,
    display,
    eliminate
)


rows_a = 'ABC'
rows_d = 'DEF'
rows_g = 'GHI'

cols_1 = '123'
cols_4 = '456'
cols_7 = '789'

digits = cols = cols_1 + cols_4 + cols_7
rows = rows_a + rows_d + rows_g

cells = cross(rows, cols)

units_cols = [cross(rows, c) for c in cols]
units_rows = [cross(r, cols) for r in rows]
units_sqrs = [cross(r, c) for r in [rows_a, rows_d, rows_g]
              for c in [cols_1, cols_4, cols_7]]

units_list = (units_cols + units_rows + units_sqrs)

# input_data = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
# input_data = '420078050701056020610900049040020510503010690610009000802000000090824500040906020'
input_data = '501009000209730015073000028005800602040027800728103000307006000810470396000002100'

cell_grid_indexes = get_cell_grid_indexes(
    cells, get_cell_grid(cells, (units_cols + units_rows + units_sqrs)))

grid = parse_input(input_data, get_initial_grid('a', cols, rows))
display(grid, cells, rows, cols)


while True:
    for cell in cells:
        grid[cell] = eliminate(cell, grid, cell_grid_indexes[cell])
        display(grid, cells, rows, cols)
    if len(''.join(list(grid.values()))) == 81:
        break

