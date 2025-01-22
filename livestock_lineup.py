import sys
from collections import defaultdict

sys.stdin = open('lineup.in', 'r')
sys.stdout = open('lineup.out', 'w')

n = int(input())


graph = defaultdict(list)

for i in range(n):
    pair = [x for x in input().split()]
    pair = (pair[0], pair[-1])
    graph[pair[0]].append(pair[1])
    graph[pair[1]].append(pair[0])


cows = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy' ,'Blue', 'Buttercup', 'Sue']

lineup = []
seen = set()

for cow in cows:
    if cow in seen:
        continue
    
    cows_len = len(graph[cow])
    
    if cows_len == 2:
        continue

    if cows_len == 0:
        lineup.append(cow)
        seen.add(cow)
        continue

    stack = [cow]
    while stack:
        cur_cow = stack.pop()
        lineup.append(cur_cow)
        seen.add(cur_cow)
        neighbors = graph[cur_cow]
        for nei in neighbors:
            graph[nei].remove(cur_cow)
            if nei not in seen:
                stack.append(nei)
                seen.add(nei)

for cow in lineup:
    print(cow)        