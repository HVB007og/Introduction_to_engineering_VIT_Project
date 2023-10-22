import math


def is_junc(cord):
    possible_places, dir2 = check_walls(cord)
    if possible_places > 2:
        return True
    else:
        pass


def printmaze(iter):
    temp = list(maze)
    temp[currentpos[0]][currentpos[1]] = iter
    for line in temp:
        print(*line)


def getcord(d, x, p=None):
    if p is None:
        pos = currentpos
    else:
        pos = p

    if d == 0:
        return [pos[0] - x, pos[1]]
    elif d == 1:
        return [pos[0] + x, pos[1]]
    elif d == 2:
        return [pos[0], pos[1] - x]
    elif d == 3:
        return [pos[0], pos[1] + x]


def check_walls(posi=0):
    if posi == 0:
        posin = list(currentpos)
    else:
        posin = posi
    direction = [0, 0, 0, 0]
    possible_places = 0

    if maze[(posin[0] - 1)][posin[1]] == 0:  # up
        possible_places += 1
        direction[0] = 1
    if maze[(posin[0] + 1)][posin[1]] == 0:  # down
        possible_places += 1
        direction[1] = 1
    if maze[posin[0]][(posin[1] - 1)] == 0:  # left
        possible_places += 1
        direction[2] = 1
    if maze[posin[0]][(posin[1] + 1)] == 0:  # right
        possible_places += 1
        direction[3] = 1

    return possible_places, direction


def length(x, y):
    # print("lengthcalled:",[currentpos[0]+x,currentpos[1]+y],'length:', end=' ')

    if x == 0 and y == 0:
        return -1
    val = math.sqrt((currentpos[0] + x - finalpos[0]) ** 2 + (currentpos[1] + y - finalpos[1]) ** 2)
    # print(val)
    return val


def check_optimal_move():
    global lastpos
    # print("called check optimal move")
    lengths = []
    if dir[0] == 1:
        lengths.append([0, length(-2, 0)])
    if dir[1] == 1:
        lengths.append([1, length(2, 0)])
    if dir[2] == 1:
        lengths.append([2, length(0, -2)])
    if dir[3] == 1:
        lengths.append([3, length(0, 2)])

    current_optimal = [0, 0]
    second_optimal = [0, 0]
    least = 100000000000
    secondleast = 100000000000
    # print('com lengths:',lengths)
    for i in lengths:
        if i[1] < least:
            current_optimal = list(i)
            least = i[1]
            lengths.pop(lengths.index(i))

    # print('com lengths:',lengths)
    if len(lengths) == 1:
        second_optimal = list(lengths[0])
    else:
        for i in lengths:
            if i[1] < secondleast:
                second_optimal = list(i)
                secondleast = i[1]

    if getcord(second_optimal[0], 2) == lastpos:
        lengths.pop(lengths.index(second_optimal))
        if len(lengths) != 0:
            second_optimal = lengths[0]
        else:
            second_optimal[0] = -1
    return current_optimal[0], second_optimal[0]


def movepos(d):
    print("movepos called:", d)

    global currentpos, lastpos
    lastpos = list(currentpos)
    if d == 0:
        currentpos = list([currentpos[0] - 2, currentpos[1]])
    elif d == 1:
        currentpos = list([currentpos[0] + 2, currentpos[1]])
    elif d == 2:
        currentpos = list([currentpos[0], currentpos[1] - 2])
    elif d == 3:
        currentpos = list([currentpos[0], currentpos[1] + 2])


def jump_to_last_junc():
    print("called jump_to_last_junc()")
    global currentpos, lastpos, movehistory
    for i in movehistory[::-1]:
        if is_junc(i[0]):
            pass

        wallcord = getcord(lastjunc[2], 1, lastpos)
        print(wallcord)
        maze[wallcord[0]][wallcord[1]] = 1
        currentpos = list(lastjunc[0])
        print(lastjunc)
        lastpos = list(lastjunc[1])

    i = int()
    for i in range(len(movehistory)):
        if movehistory[i][0] == lastjunc[0]:
            movehistory = list(movehistory[0:i])
            break


# maze = eval(input())
maze = [[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]
lastjunc = [[], [], int()]
lastpos = [5, 1]
currentpos = [5, 1]  # starting position
finalpos = [5, 13]  # final position
movehistory = [[[], []], [[], []]]
run = True
i = 0

while run and i < 50:
    printmaze(i)

    if [currentpos, lastpos] in movehistory:
        print('***************Infinite loop!***************')
        jump_to_last_junc()
    movehistory.append([currentpos, lastpos])

    if currentpos == finalpos:
        break

    print('\n', i, currentpos, 'last:', lastpos)

    noplaces, dir = check_walls()
    print('2:', noplaces, dir)

    if noplaces == 1:
        print('moving w/o option')
        if lastpos == getcord(dir.index(1), 2):
            jump_to_last_junc()
            continue
        movepos(dir.index(1))
        i += 1
        continue

    elif noplaces == 2:
        print('moving w/o option - 2')
        dir1, fallbackdir1 = check_optimal_move()
        if lastpos == getcord(dir1, 2):
            movepos(fallbackdir1)
        else:
            movepos(dir1)

    elif noplaces > 2:
        print('moving w/o option - 3')
        dir1, fallbackdir1 = check_optimal_move()
        print('dir1, fallbackdir1:', dir1, fallbackdir1)
        print(getcord(dir1, 2))
        if fallbackdir1 == -1:
            pass
        if lastpos == getcord(dir1, 2):
            lastjunc = list([list(currentpos), list(lastpos), fallbackdir1])
            movepos(fallbackdir1)

        else:
            lastjunc = list([list(currentpos), list(lastpos), dir1])
            movepos(dir1)
        print('last junction:', lastjunc)

    else:
        # run backtrack program
        pass

    i += 1

# [[0,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
#  [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,1,0,1,1,1,0,1,1,1,0,1,0,0],
#  [0,0,1,0,0,0,0,0,1,0,1,0,1,0,0],
#  [1,1,1,1,1,0,1,1,1,0,1,0,1,1,1],
#  [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
#  [1,1,1,0,1,0,0,0,1,0,1,0,1,1,1],
#  [0,0,1,0,1,0,0,0,1,0,1,0,1,0,0],
#  [0,0,1,0,1,1,1,1,1,0,1,1,1,0,0],
#  [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0]]
