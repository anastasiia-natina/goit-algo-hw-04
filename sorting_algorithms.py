import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def compare_sorting_algorithms(data):
    merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=10)
    insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=10)
    timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=10)

    print("Час сортування за допомогою сортування злиттям:", merge_time)
    print("Час сортування за допомогою сортування вставками:", insertion_time)
    print("Час сортування за допомогою Timsort:", timsort_time)

if __name__ == "__main__":

    data = [random.randint(0, 1000) for _ in range(1000)]

    compare_sorting_algorithms(data)

def merge_k_lists(lists):
    merged = []
    while any(lists):
        min_val = float('inf')
        min_idx = -1
        for i, lst in enumerate(lists):
            if lst and lst[0] < min_val:
                min_val = lst[0]
                min_idx = i
        if min_idx != -1:
            merged.append(min_val)
            lists[min_idx].pop(0)
    return merged

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)