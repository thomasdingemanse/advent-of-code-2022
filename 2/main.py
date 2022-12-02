def part_1():
    with open("C:/Users/koosk/Documents/GitHub/advent-of-code-2022/2/input_heleen.txt", "r") as file:
        #for first player A = Rock, B=Paper , C= Scisor  and for second player  X = Rock 1 point , Y = Paper 2 point , Z = Scisor 3 points
        # win = 6 , draw = 3 , lose = 0
        score_dict= {"A Z":3 ,"A Y": 8,"A X": 4,"B Z":9 ,"B Y":5 ,"B X": 1,"C Z": 6,"C Y":2 ,"C X":7 }
        total_score =0
        for line in file.readlines():
            # Add calories to the current elf's calorie count
            line = line.split("\n")[0]
            total_score += score_dict [line]
            
        print("Total score is ex 1:", total_score)

def part_2():
    with open("C:/Users/koosk/Documents/GitHub/advent-of-code-2022/2/input_heleen.txt", "r") as file:
        score_dict= {"A Z":8 ,"A Y": 4,"A X": 3,"B Z":9 ,"B Y":5 ,"B X": 1,"C Z": 7,"C Y":6 ,"C X":2 }
        total_score = 0
        for line in file.readlines():
            line = line.split("\n")[0]
            total_score += score_dict [line]
    
    print("Excersice 2 total score:",total_score )

if __name__ == "__main__":
    part_1()
    part_2()