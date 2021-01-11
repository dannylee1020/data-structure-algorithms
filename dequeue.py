import collections

DoubleEnded = collections.deque(['Mon','Tues','Wed'])

# adding elements to right
DoubleEnded.append('Thu')
print('Append at right - ')
print(DoubleEnded)
# adding elements to left
DoubleEnded.appendleft('Sun')
print('Append at left -')
print(DoubleEnded)
# deleting element from right
DoubleEnded.pop()
print('Delete at right -')
print(DoubleEnded)
#deleting element from left
DoubleEnded.popleft()
print('Delete at left')
print(DoubleEnded)