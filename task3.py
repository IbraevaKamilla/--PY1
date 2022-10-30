def delete(list_, index=None):
    ...  # TODO реализовать функцию удаления элемента из списка по индексу

#1
list_ = [0, 0, 1, 2]
middle_index = len(list_) // 2
left_list = list_[:middle_index]
right_list = list_[middle_index:]
del left_list [0]
print(left_list + right_list)

#2
list2 = [0, 1, 1, 2, 3]
middle_index = len(list2) // 2
left_list = list2[:middle_index]
right_list = list2[middle_index:]
del left_list [1]
print(left_list + right_list)

#3
list3 = [0, 1, 2, 3, 4, 4]
middle_index = len(list3) // 2
left_list = list3[:middle_index]
right_list = list3[middle_index:]
del right_list [-1] #по условию, если индекс не указан, удаляется последний элемент с индексом -1
print(left_list + right_list)