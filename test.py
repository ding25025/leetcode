rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
block = [[set() for _ in range(3)] for _ in range(3)]

for i in range(9):
    for j in range(9):
        block[i // 3][j // 3].add(1)
        print(str(i // 3) + "," + str(j // 3))
