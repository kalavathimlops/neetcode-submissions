from typing import List,Dict

def count_characters(word: str) -> Dict[str, int]:
    char_count={}

    for char in word:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char] =1
    return char_count

print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))              
