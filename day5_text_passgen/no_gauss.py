total_sum = 0
number_list = []
for number in range(1, 101):
    if number % 2 == 0:
        total_sum += number
        number_list.append(number)

print(total_sum)
print(number_list)

total_sum2 = 0
for number in range(2, 101, 2):
    total_sum2 += number

print(total_sum2)
