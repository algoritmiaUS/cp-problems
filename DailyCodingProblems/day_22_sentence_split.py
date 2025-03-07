#Pablo Moreno Moreu

"""
Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible reconstruction, return any of them. 
If there is no possible reconstruction, then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", 
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond']."""


def split_by_words(words:set, s:str) -> list:
    res=[]
    temp = ""
    for ch in s:
        temp = temp + ch
        if temp in words:
            res.append(temp)
            temp=""
    return res
        

print(split_by_words({'quick', 'brown', 'the', 'fox'}, "thequickbrownfox"))