N = int(input())

first = [1]
row = 1
found = False

while  not found:
    temp = [0] * (row + 1)
    for j in range(row + 1):
        if j == 0 or j == row:
            temp[j] = 1
        else:
            temp[j] = first[j - 1] + first[j]
        if temp[j] == N:
            found = True
            print(row,j+1)
            break
    first = temp[:]
    row += 1