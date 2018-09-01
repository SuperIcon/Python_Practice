def find_max(a_list):
    if len(a_list) == 0:
        return 0
    return max(a_list)

print(find_max([1, 2, 3]))
print(find_max([1, -1, -5]))
print(find_max([]))
