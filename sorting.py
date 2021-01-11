# different types of sorting 

def bubble_sort(lst):
    # swap the elements to sort in order
    for iter_num in range(len(lst)-1, 0, -1):
        for idx in range(iter_num):
            if lst[idx] > lst[idx+1]:
                temp = lst[idx]
                lst[idx] = lst[idx+1]
                lst[idx+1] = temp


# merge sort
def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res
        

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    middle = len(unsorted_list)//2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list  = merge_sort(right_list)
    return list(merge(left_list, right_list))
    
    
# insertion sort
def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        j = i-1
        nxt_element = input_list[i]

        while (input_list[j] > nxt_element) and (j>=0):
            input_list[j+1] = input_list[j]
            j=j-1
        input_list[j+1] = nxt_element



lst = [19,2,31,45,6,11,121,27]
lst2 = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(lst)
print(lst)
print(merge_sort(lst2))
insertion_sort(lst2)
print(lst2)