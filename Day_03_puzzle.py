import re

def get_Input():
    input = 'Day_03_input.txt'
    with open(input) as puzzle_Input:
        txt = puzzle_Input.readlines()
        corrupt_Str = ''
        for line in txt:
            corrupt_Str += line
        return corrupt_Str

def find_Muls(corrupt_Str):
    muls_Strs = re.findall("mul\(\d+,\d+\)", corrupt_Str)
    mul_Sum = 0
    for mul in muls_Strs:
        mul_Pair = mul.lstrip('mul(').rstrip(')').split(',')
        mul_Sum += int(mul_Pair[0]) * int(mul_Pair[1])
    return mul_Sum

def main():
    corrupt_Str = get_Input()
    print(find_Muls(corrupt_Str))
    corrupt_Dos = corrupt_Str.split('do()')
    do_Mul_Sum = 0
    for do in corrupt_Dos:
        do_Muls = do.split("don't()")
        do_Mul_Sum += find_Muls(do_Muls[0])
    print(do_Mul_Sum)


if __name__ == '__main__':
    main()