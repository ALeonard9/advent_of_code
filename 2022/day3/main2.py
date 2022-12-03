total_score = 0
int = 1
line_list = []

with open('input.txt') as topo_file:
    for line in topo_file:
        line_list.append(line.strip())
        if int < 3:
            int += 1
        else:
            int = 1
            common_obj = set.intersection(*map(set, line_list))
            line_list = []
            common = list(common_obj)[0]
            unicode_subtract = 64 - 26
            if common.islower():
                unicode_subtract = 96

            common_score = ord(common) - unicode_subtract

            total_score += common_score

print(total_score)
