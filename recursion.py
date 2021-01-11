# implementing binary search with recursion

lst = [8,11,15,24,56,88,131]


def bsearch(list, idx0, idxn, val):
    if (idxn < idx0):
        return None
    else:
        # midval = idx0 + ((idxn-idx0)//2)
        midval = (idxn + idx0) // 2

        if list[midval] > val:
            return bsearch(list, idx0, midval-1, val)
        elif list[midval] < val:
            return bsearch(list, midval+1, idxn, val)
        else:
            return midval

print(bsearch(lst, 0, 5, 88))
print(bsearch(lst, 0, 5, 100))

