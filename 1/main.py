import numpy as np

lines = open("./input", "r").read().split('\n')

n = []
nd = []

for i in range(len(lines)):
    str = ""
    for j in range(len(lines[i])):
        if (lines[i][j].isdigit()):
            str = str + lines[i][j]
    if(len(str) > 0):
        n.append(str)

for i in range(len(n)):
    nd.append(n[i][0] + n[i][-1])

res = [int(i) for i in nd]

print(np.sum(res))

