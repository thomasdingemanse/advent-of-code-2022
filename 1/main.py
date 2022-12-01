with open("C:/Users/koosk/Documents/GitHub/advent-of-code-2022/1/input_heleen.txt", "r") as file:
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
