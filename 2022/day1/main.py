elf = 1
calories = 0

top_elf = 0
top_elf_calories = 0

with open('input.txt') as topo_file:
    for line in topo_file:
        if line.strip():
            calories += int(line)
        else:
            print(elf, ' : ', calories)

            if calories > top_elf_calories:
                top_elf = elf
                top_elf_calories = calories

            elf += 1
            calories = 0
    print(elf, ' : ', calories)
    if calories > top_elf_calories:
        top_elf = elf
        top_elf_calories = calories
    print('The Top Elf is ', top_elf, ' with :',
          top_elf_calories, ' calories.')
