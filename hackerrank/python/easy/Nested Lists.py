if __name__ == '__main__':
    
    students_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students_list.append(student)
        
    scores = []
    for student in students_list:
        scores.append(student[1])
        
    unique_scores = list(set(scores))
    unique_scores = sorted(unique_scores)
    second_lowest = unique_scores[1]
    
    winners = []
    for student in students_list:
        name = student[0]
        score = student[1]
        if score == second_lowest:
            winners.append(name)
    
    winners = sorted(winners)
    for name in winners:
        print(name)
