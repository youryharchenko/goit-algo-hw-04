import timeit
import random


def insertion_sort_my(lst):
    sorted, unsorted = [], lst
    while len(unsorted) > 0:
        key = unsorted.pop(0)
        for i, x in enumerate(sorted):
            if key < x:
                break
        else:
            i = len(sorted)
        sorted.insert(i, key)
    return sorted    
    
def insertion_sort_old(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(lst):
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged
    

list_length = 100
min_value, max_value = -100, 100
random_lst = [random.randint(min_value, max_value) for _ in range(list_length)]
number = 100000

def main():

    
    print(insertion_sort_my([random.randint(min_value, max_value) for _ in range(10)]))
    print(insertion_sort_old([random.randint(min_value, max_value) for _ in range(10)]))
    print(merge_sort([random.randint(min_value, max_value) for _ in range(10)]))
    print(sorted([random.randint(min_value, max_value) for _ in range(10)]))
        
    code_insertion_sort_my = "insertion_sort_my(random_lst.copy())"
    time_insertion_sort_my = timeit.timeit(code_insertion_sort_my, globals=globals(), number=number)
    print(f"time_insertion_sort_my: {time_insertion_sort_my}")

    code_insertion_sort_old = "insertion_sort_old(random_lst.copy())"
    time_insertion_sort_old = timeit.timeit(code_insertion_sort_old, globals=globals(), number=number)
    print(f"time_insertion_sort_old: {time_insertion_sort_old}")

    code_merge_sort = "merge_sort(random_lst.copy())"
    time_merge_sort = timeit.timeit(code_merge_sort, globals=globals(), number=number)
    print(f"time_merge_sort: {time_merge_sort}")

    code_sorted = "sorted(random_lst.copy())"
    time_sorted = timeit.timeit(code_sorted, globals=globals(), number=number)
    print(f"time_sorted: {time_sorted}")
    
    


    
