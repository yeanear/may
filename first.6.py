def count_numbers(lst):
    count_dict = {}
    for num in lst:
        if isinstance(num, int) or isinstance(num, float):
            count_dict[num] = count_dict.get(num, 0) + 1
    return count_dict
list=[1,2,1,2,3]
result = count_numbers(list)
print(result)

