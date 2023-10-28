import math
import time


def check_in_history(coord):
    for movement in movehistory[::-1]:
        if coord == movement[0]:
            print('in History')
            return True
    else:
        print('not in History')
        return False


def check_Junction(coord):
    noplaces2, dir2 = check_walls(coord)
    if noplaces2 > 2:
        return True
    return False


def block_wall(coord, Direction):
    print("called block_wall(coord, Direction):")
    if Direction == 0:
        maze[coord[0] - 1][coord[1]] = 1
    elif Direction == 1:
        maze[coord[0] + 1][coord[1]] = 1
    elif Direction == 2:
        maze[coord[0]][coord[1] - 1] = 1
    elif Direction == 3:
        maze[coord[0]][coord[1] + 1] = 1
    printlist(maze)


def jump_to_last_junc():
    global currentpos, lastpos, movehistory
    print("called jump_to_last_junc():")
    for movement in movehistory[::-1]:
        print('  ', movement, check_Junction(movement[0]))
        if check_Junction(movement[0]):
            movehistory = list(movehistory[0: movehistory.index(movement)])
            print("new move history:")
            printlist(movehistory)
            block_wall(movement[0], movement[2])
            currentpos, lastpos = list(movement[0]), list(movement[1])
            print("jumped To", currentpos, lastpos)
            break
    else:
        # condition when no feasible path to final
        print("no path")
        return -1


def printlist(list):  # For debugging
    for line in list:
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


def length(x, y):
    # print("lengthcalled:",[currentpos[0]+x,currentpos[1]+y],'length:', end=' ')

    if x == 0 and y == 0:
        return -1
    val = math.sqrt((currentpos[0] + x - finalpos[0]) ** 2 + (currentpos[1] + y - finalpos[1]) ** 2)
    # print(val)
    return val


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


def movepos(d):
    global currentpos, lastpos
    print("movepos called:", d)

    movehistory.append([currentpos, lastpos, d])
    logichistory.append([currentpos, lastpos, d])
    lastpos = list(currentpos)
    if d == 0:
        currentpos = list([currentpos[0] - 2, currentpos[1]])
    elif d == 1:
        currentpos = list([currentpos[0] + 2, currentpos[1]])
    elif d == 2:
        currentpos = list([currentpos[0], currentpos[1] - 2])
    elif d == 3:
        currentpos = list([currentpos[0], currentpos[1] + 2])
    print("after Moving:", currentpos, lastpos)


def check_optimal_move():
    global lastpos
    print("called check optimal move", end='')
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
    # print('com lengths:', lengths)
    for i in lengths:
        if i[1] < least:
            current_optimal = list(i)
            least = i[1]
            lengths.pop(lengths.index(i))

    # print('com lengths:', lengths)
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
    print('', current_optimal[0], second_optimal[0])
    return current_optimal[0], second_optimal[0]


def change_direction(direction):
    global current_direction
    # print(current_direction, direction, ':', end='')
    if current_direction == 0 and direction == 0 or current_direction == 1 and direction == 3 or \
            current_direction == 2 and direction == 1 or current_direction == 3 and direction == 2:
        return 'Do nothing'
    if current_direction == 0 and direction == 3 or current_direction == 1 and direction == 1 or \
            current_direction == 2 and direction == 2 or current_direction == 3 and direction == 0:
        current_direction = (current_direction + 1) % 4
        return 'Turn right'
    if current_direction == 0 and direction == 2 or current_direction == 1 and direction == 0 or \
            current_direction == 2 and direction == 3 or current_direction == 3 and direction == 1:
        current_direction = (current_direction + 3) % 4
        return 'Turn left'
    if current_direction == 0 and direction == 1 or current_direction == 1 and direction == 2 or \
            current_direction == 2 and direction == 0 or current_direction == 3 and direction == 3:
        current_direction = (current_direction + 2) % 4
        return 'Turn around'
    pass


def print_clear_directions(history):
    for item in history:
        print(change_direction(item[2]), '\n  move forward once')
    pass


# maze = eval(input())  #Input Maze in a bit matrix(even i , even j values are points dont matter in logic)
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

# currentpos = eval(input())
currentpos = [5, 1]  # starting position
# finalpos = eval(input())
finalpos = [5, 13]  # final position

current_direction = 1   # For final human interpretable directions

lastpos = list(currentpos)
movehistory = []  # [[[], [], int()], [[], [], int()]]
logichistory = []

solved = False
run, i = True, int()
while run and i < 50:
    print("****************************************************************"
          "\n", i, "data:", currentpos, lastpos, "\n\nHistory:")
    printlist(movehistory)
    print()

    if currentpos == finalpos:
        print("Maze solved optimally!")
        print("shortest distance = ", len(movehistory), '\n')
        solved = True
        break

    if check_in_history(currentpos):
        if jump_to_last_junc() == -1:
            break
        pass

    noplaces, dir = check_walls()
    print('Check walls output', noplaces, dir)

    if noplaces == 0:
        break

    if noplaces == 1:
        if lastpos == getcord(dir.index(1), 2):
            if jump_to_last_junc() == -1:
                break
            continue
        movepos(dir.index(1))
        i += 1

    elif noplaces == 2:
        dir1, fallbackdir1 = check_optimal_move()
        if lastpos == getcord(dir1, 2):
            movepos(fallbackdir1)
        else:
            movepos(dir1)
        i += 1
    elif noplaces > 2:
        dir1, fallbackdir1 = check_optimal_move()
        if lastpos == getcord(dir1, 2):
            movepos(fallbackdir1)
        else:
            movepos(dir1)
        i += 1
    # time.sleep(1)


if solved:
    print_clear_directions(movehistory)
# print("\nlogic Directions:")
# print_clear_directions(logichistory)
else:
    print("Maze Not Solvable!")