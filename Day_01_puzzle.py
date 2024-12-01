def get_input():
    input = 'Day_01_input.txt'
    with open(input) as puzzle_Input:
        txt = puzzle_Input.readlines()
        raw_Input = []
        for line in txt:
            raw_Input.append(line.rstrip('\n'))
        id_List_1 = []
        id_List_2 = []
        for pair_Str in raw_Input:
            pair = pair_Str.split('   ')
            id_List_1.append(int(pair[0]))
            id_List_2.append(int(pair[1]))
        id_List_1.sort()
        id_List_2.sort()
        return id_List_1, id_List_2

def find_Dif(id_List_1, id_List_2):
    difs = []
    for index in range(len(id_List_1)):
        difs.append(abs(id_List_1[index] - id_List_2[index]))
    return sum(difs)

def find_Sim(id_List_1, id_List_2):
    sims = []
    for id in id_List_1:
        sims.append(id * id_List_2.count(id))
    return sum(sims)

def main():
    id_List_1, id_List_2 = get_input()
    print(find_Dif(id_List_1, id_List_2))
    print(find_Sim(id_List_1, id_List_2))

if __name__ == '__main__':
    main()