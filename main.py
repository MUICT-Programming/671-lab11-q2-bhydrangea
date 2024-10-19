def summation(lst1, lst2):
    updated_list = [x + y for x, y in zip(lst1, lst2)]
    return updated_list

def find_min_max(updated_list):
    return min(updated_list), max(updated_list)

n = int(input())
lst1 = [int(input()) for k in range(n)]
lst2 = [int(input()) for k in range(n)]

updated_list = summation(lst1, lst2)
min_value, max_value = find_min_max(updated_list)

print(updated_list)
print((min_value, max_value))
