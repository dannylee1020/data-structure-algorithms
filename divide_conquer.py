# implementing binary search using divide and conquer

lst = [2,7,19,34,53,72]

def bsearch(list, val):
    list_size = len(list) - 1
    idx0 = 0 
    idxn = list_size

    while idx0 <= idxn:
        midval = (idx0 + idxn) // 2

        if val == lst[midval]:
            return midval
        
        if val > lst[midval]:
            idx0 = midval+1
        else:
            idxn = midval-1
        
        if idx0 > idxn:
            return None


print(bsearch(lst, 34))
print(bsearch(lst, 5))


