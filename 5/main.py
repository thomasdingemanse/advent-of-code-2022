part = 2

with open("./input.txt", "r") as input:
    lines = input.readlines()
    fat_stacks = []
    
    for i in range(9):
        fat_stacks.append([])
    
    for line in range(8):
        position = 1
    
        for col in range(9):
            box = lines[line][position]
            
            if box != " ":
                fat_stacks[col].append(box)

            position += 4

    for fat_stack in fat_stacks:
        fat_stack.reverse()

    for line in lines[10:]:
        _, quantity, _, source, _, destination = line.split(" ")

        quantity = int(quantity)
        source = int(source)
        destination = int(destination)
        
        if part == 1:
            for i in range(quantity):
                crate = fat_stacks[source - 1].pop()
                fat_stacks[destination - 1].append(crate)
        else:
            crates = []
            for i in range(quantity):
                crate = fat_stacks[source - 1].pop()
                crates.append(crate)
            crates.reverse()
            for crate in crates:
                fat_stacks[destination - 1].append(crate)

        for i, fat_stack in enumerate(fat_stacks):
            print(i, " ".join(fat_stack))
        print()

    for fat_stack in fat_stacks:
        if len(fat_stack) > 0:
            print(fat_stack[-1], end="")
