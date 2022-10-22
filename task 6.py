# ПЕРЕДЕЛАННОЕ ЗАДАНИЕ 
list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
list_for_sort =  [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# новый список для сортировки
list_for_sort.sort() #сортировка списка по возрастанию
print (list_for_sort)
# [-100, -93, -92, -90, -85, -45, -44, -36, -22, -14, -8, -2, -1, 2, 8, 25, 38, 53, 67, 90]
# максимальный элемент списка это 90. его индекс равен -1
min(i for i in list_numbers if i > 0) #поиск минимального положительного элемента
print(min)
print(list_for_sort.index(2))
# 13
print(list_for_sort.index(90))
# -1
print(list_numbers.index(2))
# 0
print(list_numbers.index(90))
# 9
list_numbers [9], list_numbers [0] = list_numbers [0], list_numbers [9]
print (list_numbers)
