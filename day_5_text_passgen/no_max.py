student_scores = input("Input a list of students scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

current_max_score = 0  # 0 is the minimum score possible
current_min_score = 100  # 100 is the maximum score possible
for score in student_scores:
    if score > current_max_score:
        current_max_score = score
    if score < current_min_score:
        current_min_score = score

print(f"The min score is {current_min_score} of 100.")
print(f"The max score is {current_max_score} of 100.")
