my_list = [1, 2, 3, 4, 5]

new_list = []
for x in my_list:
    new_list.append(x * 2)

print(new_list)

my_list2 = [1, 2, 3, 4, 5]


def multi_2(x):
    return x * 2


new_list2 = list(map(multi_2, my_list2))
print(new_list2)
print(sorted(new_list2, reverse=True))

new_list2 = map(lambda x: x*2, my_list2)
print(list(new_list2))
