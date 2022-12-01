def part_1():
    with open("./input.txt", "r") as file:
        most_calories = 0
        current_calories = 0

        for line in file.readlines():
            # Add calories to the current elf's calorie count
            if line != '\n':
                current_calories += int(line)
                        
            # Empty line, start counting again
            else:
                if current_calories > most_calories:
                    most_calories = current_calories
                current_calories = 0
        
        print(most_calories)

def part_2():
    with open("./input.txt", "r") as file:
        most_calories = 0
        second_most_calories = 0
        third_most_calories = 0
        current_calories = 0

        for line in file.readlines():
            if line != '\n':
                current_calories += int(line)
                        
            else:
                if current_calories > most_calories:
                    third_most_calories = second_most_calories
                    second_most_calories = most_calories
                    most_calories = current_calories
                elif current_calories > second_most_calories:
                    third_most_calories = second_most_calories
                    second_most_calories = current_calories
                elif current_calories > third_most_calories:
                    third_most_calories = current_calories
                
                current_calories = 0

        print(most_calories + second_most_calories + third_most_calories)

if __name__ == "__main__":
    part_1()
    part_2()