list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_index = 0
max_number = list_numbers[max_index]

for i, current_number in enumerate (list_numbers):
    max_number = list_numbers[max_index]
    if current_number > max_number:
        max_index = i
        max_number = list_numbers[max_index]
    print (max_number, max_index)

min_index = 0
min_number = list_numbers [min_index]
for i, current_number in enumerate (list_numbers):
    min_number = list_numbers [min_index]
    if current_number < min_number:
        min_index = i
        min_number = list_numbers [min_index]
    print(min_number, min_index)

max_number, min_number = min_number, max_number
print(min_number, max_number)
print(list_numbers)

max_number, min_number = "max_number", "min_number"
max_number, min_number = min_number, max_number
print(max_number, min_number)

