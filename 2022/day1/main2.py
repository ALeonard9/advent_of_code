elf = 1
calories = 0

top_elf = 0
top_elf_calories = 0

elf_dict = {}

with open('input.txt') as topo_file:
    for line in topo_file:
        if line.strip():
            calories += int(line)
        else:
            print(elf, ' : ', calories)
            elf_dict[elf] = calories

            if calories > top_elf_calories:
                top_elf = elf
                top_elf_calories = calories

            elf += 1
            calories = 0
    print(elf, ' : ', calories)
    elf_dict[elf] = calories
    if calories > top_elf_calories:
        top_elf = elf
        top_elf_calories = calories
    print('The Top Elf is ', top_elf, ' with :',
          top_elf_calories, ' calories.')

    def sort_dict_by_value(d, reverse=False):
        return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))
    print("Original dictionary elements:")
    print(elf_dict)
    print("\nSort (ascending) the said dictionary elements by value:")
    print(sort_dict_by_value(elf_dict, True))
