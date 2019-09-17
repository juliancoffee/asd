import itertools
import random
import time
import sys

setup = time.time()

n = int(sys.argv[1])

work_matrix = [[random.randint(1, 11) for i in range(n)] for j in range(n)]
for i in range(n):
    print(i, work_matrix[i])
print("\n")

perms = itertools.permutations(range(n))

res = float("inf")
for perm in perms:
    plan = []
    for task in range(n):
            plan.append(work_matrix[perm[task]][task])
    if sum(plan) < res:
        res = sum(plan)
        print("For {} => {}".format(perm, plan))
print("Result = {}".format(res))
print("Time = {}".format(time.time() - setup))
