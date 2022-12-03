total_score = 0

with open('test_input.txt') as topo_file:
    for line in topo_file:
        line_length = len(line)
        chars = line_length
        half = int(chars/2)
        first_line = line[0:int(half)]
        second_line = line[half:chars]
        common = ''.join(set(first_line).intersection(second_line))

        unicode_subtract = 64 - 26
        if common.islower():
            unicode_subtract = 96

        common_score = ord(common) - unicode_subtract

        total_score += common_score

print(total_score)
