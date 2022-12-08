import argparse


def main(argv=None):
    # Parse file name from args
    file_name = get_file_name(argv)

    # read in the input from the file
    with open(file_name, 'r') as txt_file:
        grid = [line.strip() for line in txt_file]

    # Part 1
    # Calculate the number of trees that are visible from outside the grid
    # trees_visible = 0
    # for i, row in enumerate(grid):
    #     for j, col in enumerate(row):
    #         if is_visible(grid, i, j, grid[i][j]):
    #             trees_visible+=1
    # print(f'Trees visible: {trees_visible}')

    # Part 2
    # Calculate the scenic score (how many trees can be seen from a given point)
    # For each tree in the grid
    max_score = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            cur_score = get_scenic_score(grid, i, j, grid[i][j])
            if cur_score > max_score:
                max_score = cur_score
    print(f'Scenic score: {max_score}')

    return 0

def is_visible(grid, row, col, cur_height):
    # For a given coord in the grid, is it visible from any side?
    if is_visible_above(grid, row, col, cur_height) or \
        is_visible_below(grid, row, col, cur_height) or \
        is_visible_left(grid, row, col, cur_height) or \
        is_visible_right(grid, row, col, cur_height):
            # print(f'Visible!  {row},{col} - height: {cur_height}')
            return True
    return False

def is_visible_above(grid, row, col, cur_height):
    for i in range(row):
        if grid[i][col] >= cur_height:
            return False
    return True
        
def is_visible_below(grid, row, col, cur_height):
    for i in range(row+1, len(grid)):
        if grid[i][col] >= cur_height:
            return False
    return True

def is_visible_left(grid, row, col, cur_height):
    for i in range(col):
        if grid[row][i] >= cur_height:
            return False
    return True
        
def is_visible_right(grid, row, col, cur_height):
    for i in range(col+1, len(grid)):
        if grid[row][i] >= cur_height:
            return False
    return True

def get_scenic_score(grid, row, col, cur_height):
    # get the scenic score for a given coord in the grid
    score = scenic_above(grid, row, col, cur_height) * \
        scenic_below(grid, row, col, cur_height) * \
        scenic_left(grid, row, col, cur_height) * \
        scenic_right(grid, row, col, cur_height)
    # print(f'{row},{col} {cur_height}- Score: {score}')
    return score

def scenic_above(grid, row, col, cur_height):
    trees = 0
    for i in range(row-1, -1, -1):
        trees += 1
        if grid[i][col] >= cur_height:
            return trees
    return trees
        
def scenic_below(grid, row, col, cur_height):
    trees = 0
    for i in range(row+1, len(grid)):
        trees += 1
        if grid[i][col] >= cur_height:
            return trees
    return trees

def scenic_left(grid, row, col, cur_height):
    trees = 0
    for i in range(col-1, -1, -1):
        trees += 1
        if grid[row][i] >= cur_height:
            return trees
    return trees
        
def scenic_right(grid, row, col, cur_height):
    trees = 0
    for i in range(col+1, len(grid)):
        trees += 1
        if grid[row][i] >= cur_height:
            return trees
    return trees

def get_file_name(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="Input file name")
    args = parser.parse_args(argv)
    return args.filename

if __name__ == "__main__":
    main()