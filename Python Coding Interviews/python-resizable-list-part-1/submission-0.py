from typing import List

def append_elements(arra1:List[int],arr2:List[int]) -> List[int]:
    for elements in arr2:
        arr1.append(elements)
    return arr1    