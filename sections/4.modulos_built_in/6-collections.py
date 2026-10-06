from collections import Counter, namedtuple, deque
from operator import itemgetter

fruits = ["Maça", "Banana", "Uva", "Pêra", "Banana", "Uva", "Maça", "Laranja", "Abacaxi"]

print(fruits)
print(Counter(fruits))

game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("Fifa 23", 90.50, 8.5)
g2 = game("Resident Evil 4 Remake", 300, 10.0)
print(g1)
print(g2)

students = {"Pedro": 23, "Ana": 22, "Ronaldo": 26}
a = sorted(students.items(), key = itemgetter(0))
print(a)

deq = deque([20, 40, 60, 80])
deq.appendleft(10)
deq.append(10)
deq.popleft()
print(deq)