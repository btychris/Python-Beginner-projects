# stacks

stk = []
print(stk)

# Append to top of stack - O(1)

stk.append(5)
stk.append(9)
print(stk)

# Pop from stack - O(1)
x = stk.pop()
print(x)
print(stk)

# Ask whats on top of the stack - O(1)
print(stk[:-1])

# Ask something is in the stack - O(1)
if stk:
    print(True)

# Queues - First In First Out (Fifo)

from collections import deque as r

q = r()

print(q)

# Enqueue - Add element to the right - O(1)

q.append(5)
q.append(6)
q.append(9)
q.append(2)
q.append(1)
print(q)

# Deque (pop left) - Remove element from the left - O(1)
q.popleft()
print(q)

# Peek from left side - O(1)
print(q[0])

# Peek from left side - O(1)
print(q[-1])
