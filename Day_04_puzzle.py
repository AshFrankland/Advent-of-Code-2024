def get_Input():
    input = 'Day_04_input.txt'
    with open(input) as puzzle_Input:
        txt = puzzle_Input.readlines()
        raw_Input = []
        for line in txt:
            raw_Input.append(line.rstrip('\n'))
        grid_Height = len(raw_Input)
        grid_Width = len(raw_Input[0])
        grid_Dict = {}
        for y in range(grid_Height):
            for x in range(grid_Width):
                grid_Dict[(x, y)] = raw_Input[y][x]
        for x in range(grid_Width + 2):
            grid_Dict[(x - 1, -1)] = '*'
            grid_Dict[(x - 1, grid_Height)] = '*'
        for y in range(grid_Height):
            grid_Dict[(-1, y)] = '*'
            grid_Dict[(grid_Width, y)] = '*'
        return grid_Width, grid_Height, grid_Dict

def find_Xmas(grid_Width, grid_Height, grid_Dict):
    xmas_Count = 0
    for y in range(grid_Height):
        for x in range(grid_Width):
            if grid_Dict[(x, y)] == 'X':
                if grid_Dict[(x - 1, y - 1)] == 'M':
                    if grid_Dict[(x - 2, y - 2)] == 'A':
                        if grid_Dict[(x - 3, y - 3)] == 'S':
                            xmas_Count += 1
                if grid_Dict[(x, y - 1)] == 'M':
                    if grid_Dict[(x, y - 2)] == 'A':
                        if grid_Dict[(x, y - 3)] == 'S':
                            xmas_Count += 1
                if grid_Dict[(x + 1, y - 1)] == 'M':
                    if grid_Dict[(x + 2, y - 2)] == 'A':
                        if grid_Dict[(x + 3, y - 3)] == 'S':
                            xmas_Count += 1
                if grid_Dict[(x - 1, y)] == 'M':
                    if grid_Dict[(x - 2, y)] == 'A':
                        if grid_Dict[(x - 3, y)] == 'S':
                            xmas_Count += 1
                if grid_Dict[(x + 1, y)] == 'M':
                    if grid_Dict[(x + 2, y)] == 'A':
                        if grid_Dict[(x + 3, y)] == 'S':
                            xmas_Count += 1
                if grid_Dict[(x - 1, y + 1)] == 'M':
                    if grid_Dict[(x - 2, y + 2)] == 'A':
                        if grid_Dict[(x - 3, y + 3)] == 'S':
                            xmas_Count += 1
                if grid_Dict[(x, y + 1)] == 'M':
                    if grid_Dict[(x, y + 2)] == 'A':
                        if grid_Dict[(x, y + 3)] == 'S':
                            xmas_Count += 1
                if grid_Dict[(x + 1, y + 1)] == 'M':
                    if grid_Dict[(x + 2, y + 2)] == 'A':
                        if grid_Dict[(x + 3, y + 3)] == 'S':
                            xmas_Count += 1
    return xmas_Count

def find_X_Mas(grid_Width, grid_Height, grid_Dict):
    x_Mas_Count = 0
    for y in range(grid_Height):
        for x in range(grid_Width):
            if grid_Dict[(x, y)] == 'A':
                if grid_Dict[(x - 1, y - 1)] == 'M' and grid_Dict[(x - 1, y + 1)] == 'M' and grid_Dict[(x + 1, y - 1)] == 'S' and grid_Dict[(x + 1, y + 1)] == 'S':
                    x_Mas_Count += 1
                elif grid_Dict[(x - 1, y - 1)] == 'M' and grid_Dict[(x + 1, y - 1)] == 'M' and grid_Dict[(x - 1, y + 1)] == 'S' and grid_Dict[(x + 1, y + 1)] == 'S':
                    x_Mas_Count += 1
                elif grid_Dict[(x + 1, y - 1)] == 'M' and grid_Dict[(x + 1, y + 1)] == 'M' and grid_Dict[(x - 1, y - 1)] == 'S' and grid_Dict[(x - 1, y + 1)] == 'S':
                    x_Mas_Count += 1
                elif grid_Dict[(x + 1, y + 1)] == 'M' and grid_Dict[(x - 1, y + 1)] == 'M' and grid_Dict[(x + 1, y - 1)] == 'S' and grid_Dict[(x - 1, y - 1)] == 'S':
                    x_Mas_Count += 1
    return x_Mas_Count

def main():
    grid_Width, grid_Height, grid_Dict = get_Input()
    print(find_Xmas(grid_Width, grid_Height, grid_Dict))
    print(find_X_Mas(grid_Width, grid_Height, grid_Dict))

if __name__ == '__main__':
    main()