from aoclib import *
DAY = 6
PART = 1

pInp = get_input(DAY)
ans = 0

points = set()

for i in range(len(pInp)):
    pInp[i] = list(pInp[i])

dir = 0

gx = 0
gy = 0

for i in range(len(pInp)):
    for j in range(len(pInp[0])):
        if pInp[i][j] == '^':
            gx = i
            gy = j
            break


while (gx < len(pInp) and gx >= 0 and gy >= 0 and gy < len(pInp[0])):
    try:
        match (dir):
            case 0:
                if gx == 0:
                    break
                if pInp[gx-1][gy] == '#':
                    dir = 1
                else:
                    gx -= 1

            case 1:
                if gy == len(pInp[0]) - 1:
                    break
                if pInp[gx][gy+1] == '#':
                    dir = 2
                else:
                    gy += 1

            case 2:
                if gx == len(pInp) - 1:
                    break
                if pInp[gx+1][gy] == '#':
                    dir = 3
                else:
                    gx += 1

            case 3:
                if gy == 0:
                    break
                if pInp[gx][gy-1] == '#':
                    dir = 0
                else:
                    gy -= 1

        points.add((gx, gy))

    except IndexError:
        break
            

ans = len(points)
submit(DAY, PART, ans)