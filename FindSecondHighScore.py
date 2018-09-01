def second_highest(students):
    student_rank = []
    for student in students:
        num = 0
        for student1 in students:
            if student[0] == student1[0]:
                continue
            if student[1] < student1[1]:
                num += 1
        new = [student[0], num]
        student_rank.append(new)
    
    for student in student_rank:
        if student[1] == 1:
            print(student[0])


students = [['Jerry', 80], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]
second_highest(students)