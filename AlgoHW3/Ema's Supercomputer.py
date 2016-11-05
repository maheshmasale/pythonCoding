#https://www.hackerrank.com/challenges/two-pluses?h_r=next-challenge&h_v=zen

#!/bin/python3

def get_item(grid, position):
    return grid[position[0]][position[1]]

def get_positions(grid, position, offset_amt=1):
    positions = []
    positions.append(get_position(grid, position, 'up', offset_amt))
    positions.append(get_position(grid, position, 'down', offset_amt))
    positions.append(get_position(grid, position, 'left', offset_amt))
    positions.append(get_position(grid, position, 'right', offset_amt))
    return positions

def get_position(grid, position, offset, offset_amt=1):
    posr, posc = position
    if offset == 'up': posr -= offset_amt
    elif offset == 'left': posc -= offset_amt
    elif offset == 'down': posr += offset_amt
    elif offset == 'right': posc += offset_amt
    if ((posr < 0 or posr > len(grid)-1) or
        (posc < 0 or posc > len(grid[0])-1)):
        return None
    return (posr, posc)

def compare_positions(positions_1, positions_2):
    for position in positions_1:
        if position in positions_2:
            return True
    return False

# retrieve input and populate grid
n, m = [int(x) for x in input().strip().split(' ')]

grid = []
for row in range(n):
    grid.append(list(input().strip()))

# search grid for all valid pluses
valid_pluses = []
for row in range(1,n-1):
    for column in range(1,m-1):
        current_position = (row, column)
        if get_item(grid, current_position) == 'B':
            continue
        offset_amt = 1
        positions_queue = []
        while True:
            positions = get_positions(grid, current_position, offset_amt)
            if None in positions: break
            items = [get_item(grid, position) for position in positions]
            if 'B' in items: break
            positions_queue.extend(positions)
            valid_pluses.append(((offset_amt * 4) + 1, positions_queue + [current_position]))
            offset_amt += 1

# process the valid pluses for the max product
if not valid_pluses:
    # there were no valid pluses. still check if there are any Gs
    count_g = 0
    for row in grid:
        count_g += row.count('G')
    print(1) if count_g >= 2 else print(0)
elif len(valid_pluses) == 1:
    print(valid_pluses[0][0])
else:
    # need to find max products without re-using positions.
    valid_pluses = list(reversed(sorted(valid_pluses)))
    products = []
    for i in range(len(valid_pluses)):
        current_plus = valid_pluses[i]
        comparison_pluses = valid_pluses[i+1:]
        for comparison_plus in comparison_pluses:
            if compare_positions(current_plus[1], comparison_plus[1]) != True:
                products.append(current_plus[0] * comparison_plus[0])
                break
        else:
            products.append(current_plus[0] * 1)
    print(max(products))