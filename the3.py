import sys
import copy

map_path = sys.argv[1]
with open(map_path , 'r') as map_data :
    map_first = []
    for line in map_data.readlines() :
        map_first.append(line.strip())

rules_path = sys.argv[2]
with open(rules_path , 'r') as rules_data :
    rules = []
    for line in rules_data.readlines() :
        rules.append(line.strip())

gen = int(sys.argv[3])
map_second = copy.deepcopy(map_first)

i = 0
while i < gen :
    for ele in rules :
        obj_first = ele[0]
        opr = ele[1]
        num = int(ele[2])
        obj_last = ele[3]

        for y in range(len(map_first)) :
            for x in range(len(map_first[0])) :
                if map_first[y][x] == obj_first:
                    count = 0
                    if y != len(map_first) - 1 :
                        if map_first[y + 1][x] == '*':
                            count += 1

                    if y != 0:
                        if map_first[y - 1][x] == '*':
                            count += 1

                    if x != len(map_first[0]) - 1:
                        if map_first[y][x + 1] == '*':
                            count += 1

                    if x != 0:
                        if map_first[y][x - 1] == '*':
                            count += 1

                    if y != len(map_first) - 1 and x != len(map_first[0]) - 1:
                        if map_first[y + 1][x + 1] == '*':
                            count += 1

                    if y != len(map_first) - 1 and x != 0:
                        if map_first[y + 1][x - 1] == '*':
                            count += 1

                    if y != 0 and x != len(map_first[0]) - 1:
                        if map_first[y - 1][x + 1] == '*':
                            count += 1

                    if y != 0 and x != 0:
                        if map_first[y - 1][x - 1] == '*':
                            count += 1

                    lst_map2 = []
                    for char in map_second[y] :
                        lst_map2.append(char)

                    if opr == '<':
                        if count < num:
                            lst_map2[x] = obj_last

                    if opr == '>':
                        if count > num:
                            lst_map2[x] = obj_last

                    if opr == '=':
                        if count == num:
                            lst_map2[x] = obj_last

                    new_y = ''
                    for elements in lst_map2 :
                        new_y += elements

                    map_second[y] = new_y
    map_first = copy.deepcopy(map_second)

    i += 1

result = ''
for l in map_second :
    result += l + '\n'

print result[:-1]








