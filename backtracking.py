
def permute(list, s):
    if list == 1:
        return s
    else:
        return [x+y for x in permute(1, s) for y in permute(list -1, s)]


lst =['a','b','c']
print(permute(1,lst))
print(permute(2, lst))
print(permute(3, lst))
