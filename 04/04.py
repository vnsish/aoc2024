def part1(file):
    with open(file,'r') as fp:
        words = fp.read()

    mat = []
    for line in words.splitlines():
        mat.append([x for x in line])

    total = 0

    x = len(mat)
    y = len(mat[0])
    
    for i in range(x):
        for j in range(y):
            if (j < x-3 and mat[i][j] == 'X' and  mat[i][j+1] == 'M' and mat[i][j+2] == 'A' and mat[i][j+3] == 'S'):
                total += 1
            if (j > 2 and mat[i][j] == 'X' and  mat[i][j-1] == 'M' and mat[i][j-2] == 'A' and mat[i][j-3] == 'S'):
                total += 1
            if (i < y-3 and mat[i][j] == 'X' and  mat[i+1][j] == 'M' and mat[i+2][j] == 'A' and mat[i+3][j] == 'S'):
                total += 1
            if (i > 2 and mat[i][j] == 'X' and  mat[i-1][j] == 'M' and mat[i-2][j] == 'A' and mat[i-3][j] == 'S'):
                total += 1
            if (j < x-3 and i < y-3 and mat[i][j] == 'X' and  mat[i+1][j+1] == 'M' and mat[i+2][j+2] == 'A' and mat[i+3][j+3] == 'S'):
                total += 1
            if (j > 2 and i > 2 and mat[i][j] == 'X' and  mat[i-1][j-1] == 'M' and mat[i-2][j-2] == 'A' and mat[i-3][j-3] == 'S'):
                total += 1
            if (j < x-3 and i > 2 and mat[i][j] == 'X' and  mat[i-1][j+1] == 'M' and mat[i-2][j+2] == 'A' and mat[i-3][j+3] == 'S'):
                total += 1
            if (i < y-3 and j > 2 and mat[i][j] == 'X' and  mat[i+1][j-1] == 'M' and mat[i+2][j-2] == 'A' and mat[i+3][j-3] == 'S'):
                total += 1
    print(total)

def part2(file):
    with open(file,'r') as fp:
        words = fp.read()

    mat = []
    for line in words.splitlines():
        mat.append([x for x in line])

    total = 0

    x = len(mat)
    y = len(mat[0])

    for i in range(1, x-1):
        for j in range(1, y-1):
            if ((mat[i][j] == "A" and mat[i+1][j+1] == 'S' and mat[i-1][j-1] == 'M') or (mat[i][j] == "A" and mat[i+1][j+1] == 'M' and mat[i-1][j-1] == 'S')) and (
                (mat[i][j] == "A" and mat[i+1][j-1] == 'S' and mat[i-1][j+1] == 'M') or (mat[i][j] == "A" and mat[i+1][j-1] == 'M' and mat[i-1][j+1] == 'S')):
                    total += 1
    
    print(total)

part1('input')
part2('input')