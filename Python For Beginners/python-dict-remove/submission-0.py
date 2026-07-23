from typing import List,Dict

def remove_keys(my_dict:Dict[str,int],keys:List[str]) ->Dict[str,int]:
    for key in keys:
        if key in my_dict:
            my_dict.pop(key)
    return my_dict

print(remove_keys({"a":1,"b":2,"c":3},["a","c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))      