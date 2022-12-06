from pathlib import Path
from heapq import heapify, heappush, heappop

inventory = Path('input.csv').read_text().splitlines()

ranking = []
heapify(ranking)
res1, res2, temp = 0, 0, 0

for food in inventory:
    if not food:
        res1 = max(res1, temp)
        heappush(ranking, temp * -1)
        temp = 0
    else:
        temp += int(food)

for i in range(3):
    res2 += heappop(ranking) * -1

print(f"Part one: {res1}")
print(f"Part one: {res2}")