from typing import List

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
    return my_list.append(elements)

print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))    