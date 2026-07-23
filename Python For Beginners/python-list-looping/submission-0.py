from typing import List

def count_x(nums:List[int],x:int) ->int:
    count =0
    for i in nums:
        if i in x:
            count +=1
    return count        