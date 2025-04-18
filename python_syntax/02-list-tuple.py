
test_list = []

print(test_list)

test_list2 = list()

print(test_list2)

test_list2.append(2)

print(test_list2)

test_list2.append(89)

print(test_list2)

test_list3 = [1, 6, 3, 2, 7, 5, 4]

test_list3.sort()

print(test_list3)

test_list3.reverse()

print(test_list3)

test_list3.sort(reverse=True)

print(test_list3)

sorted_list = sorted(test_list3)

print(sorted_list)

print(test_list3)

sorted_list2 = sorted(test_list3, reverse=True)

print(sorted_list2)

print(test_list3)

insert_list = []

insert_list.insert(1, 3)

print(insert_list)

insert_list.insert(1, 4)

print(insert_list)

insert_list.insert(1, 6)

print(insert_list)

insert_list.remove(4)

print(insert_list)

insert_list.pop()

print(insert_list)

mock_list = [1, 2, 3, 4, 5]

print(mock_list.pop(4))

print(mock_list)

count_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count_list.extend([11, 12, 13, 14, 15])

print(count_list)

count_list += [16, 17, 18, 19, 20]

print(count_list)


if __name__ == "__main__" :
    pass