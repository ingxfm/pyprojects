student_heights = input("Input a list of students heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

####
quantity_items = 0
sum_items = 0
for item in student_heights:
    quantity_items += 1
    sum_items += item

print(quantity_items)
print(sum_items)
print(f"{round(sum_items / quantity_items, 2)} cm")
