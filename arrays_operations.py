l1 = [4, 2, 12, 3, 90, 45]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

l2 = [(1, 2), (4, 20), (2, 90)]

print(l2)

from collections import deque
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

c1 = fruits.count('tangerine')
print(c1)

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

print([(x, y) for x in range(3) for y in range(3)])

vec = [[1, 2, 3], [4, 5, 6]]

print([l1 for x in vec for l1 in x])

