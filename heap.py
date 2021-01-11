# creating a heap in python
import heapq

H = [21,1,45,78,3,5]

heapq.heapify(H)
print(H)

# inserting into heap 
heapq.heappush(H,8)
print(H)

# removing from heap 
heapq.heappop(H)
print(H)

# replacing in a heap
heapq.heapreplace(H,6)
print(H)