fully_contained = 0
overlapping = 0

with open("./input.txt", "r") as input:
    for line in input.readlines():
        line = line.rstrip()
        section_assignments = line.split(",", maxsplit = 1)
        
        elves = []

        for section_assignment in section_assignments:
            min_max = section_assignment.split("-", maxsplit = 1)
            elves.append([int(value) for value in min_max])
        
        if elves[0][0] <= elves[1][0] and elves[0][1] >= elves[1][1]:
            fully_contained += 1
            overlapping += 1
        elif elves[0][0] >= elves[1][0] and elves[0][1] <= elves[1][1]:
            fully_contained += 1
            overlapping += 1
        elif elves[0][0] <= elves[1][0] and elves[0][1] >= elves[1][0]:
            overlapping += 1
        elif elves[0][0] <= elves[1][1] and elves[0][1] >= elves[1][1]:
            overlapping += 1

print(f"{fully_contained} assignment pairs fully contain the other.")
print(f"{overlapping} assignment pairs overlap.")
