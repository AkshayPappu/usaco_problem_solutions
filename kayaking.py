import sys

sys.stdin = open("test.in", "r")
sys.stdout = open("test.out", "w")

n = int(input()) * 2
weights = sorted([int(x) for x in input().split()])

min_instability = float('inf')
for i in range(n):
    for j in range(i + 1, n):
        
        rest_of_weights = [weights[v] for v in range(n) if v != i and v != j]
        cur_instability = 0
        for k in range(0, n - 2, 2):
            cur_instability += rest_of_weights[k + 1] - rest_of_weights[k]
        min_instability = min(min_instability, cur_instability)

print(min_instability)