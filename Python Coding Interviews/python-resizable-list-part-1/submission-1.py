from typing import List

def append_elements(arra1:List[int],arr2:List[int]) -> List[int]:
    for elements in arr2:
        arr1.append(elements)
    return arr1
def pop_n(arr:List[int],n:int) -> List[int]:
          while n >0 and arr:
            arr.pop()
            n = -1
          return arr
def insert_at(arr:List[int],index:int,element:int)->List[int]:
          if index <0 or index >= len(arr):
            arr.append(element)
          else:
            arr.insert(index,element)
          return arr         