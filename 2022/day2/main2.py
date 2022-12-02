points = 0
total = 0
total_points = 0

with open('input.txt') as topo_file:
    for line in topo_file:
        match_list = line.split()
        for item in match_list:
            match item:
                case 'X':
                    points = 0
                    match opp:
                        case 'A':
                            points += 3
                        case 'B':
                            points += 1
                        case 'C':
                            points += 2
                    total_points += points
                case 'Y':
                    points = 3
                    match opp:
                        case 'A':
                            points += 1
                        case 'B':
                            points += 2
                        case 'C':
                            points += 3
                    total_points += points
                case 'Z':
                    points = 6
                    match opp:
                        case 'A':
                            points += 2
                        case 'B':
                            points += 3
                        case 'C':
                            points += 1
                    total_points += points
                case _:
                    opp = item
                    points = 0
print(total_points)
