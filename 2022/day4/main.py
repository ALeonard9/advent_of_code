total_score = 0

with open('input.txt') as topo_file:
    for line in topo_file:
        comma = int(line.find(','))
        line_end = len(line)
        elf1 = line[0:comma]
        elf1_start = int(elf1[0:elf1.find('-')])
        elf1_end = int(elf1[elf1.find('-')+1:comma])

        elf2 = line[comma+1:line_end]
        elf2_start = int(elf2[0:elf2.find('-')])
        elf2_end = int(elf2[elf2.find('-')+1:line_end])

        if (elf1_start <= elf2_start and elf1_end >= elf2_end) or (elf1_start >= elf2_start and elf1_end <= elf2_end):
            total_score += 1

print('Total Score: ', total_score)
