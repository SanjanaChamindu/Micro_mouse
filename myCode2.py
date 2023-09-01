from queue import PriorityQueue

########################################################################
# Maze variables. Not in the original code

#                    0  1  2  3  4  5  6  7  8  9  10 11 12 13
horizontal_walls = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 0
                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],  # 1
                    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0],  # 2
                    [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],  # 3
                    [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],  # 4
                    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0],  # 5
                    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 6
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 7
                    [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],  # 8
                    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],  # 9
                    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],  # 10
                    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],  # 11
                    [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0],  # 12
                    [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],  # 13
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]  # 14

#                  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14
vertical_walls = [[1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],    # 0
                  [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1],    # 1
                  [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],    # 2
                  [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1],    # 3
                  [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],    # 4
                  [1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],    # 5
                  [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],    # 6
                  [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1],    # 7
                  [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],    # 8
                  [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],    # 9
                  [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],    # 10
                  [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],    # 11
                  [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1],    # 12
                  [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1]]    # 13

maze = [horizontal_walls, vertical_walls]
########################################################################

goals_ = ((6, 6), (7, 6), (6, 7), (7, 7))
h_walls = [[1 for i in range(14)] for j in range(15)]
v_walls = [[1 for i in range(15)] for j in range(14)]


def h_value(cell, goals):
    value = 256
    for i in goals:
        if (abs(i[0]-cell[0]) + abs(i[1]-cell[1])) <= value:
            value = abs(i[0]-cell[0]) + abs(i[1]-cell[1])
    return value


def go_from_to(start, goals, h_walls_, v_walls_, maze_):
    squares = [[float('inf') for i in range(14)] for j in range(14)]
    open_ = PriorityQueue()
    open_.put((h_value(start, goals), start))
    squares[start[1]][start[0]] = h_value(start, goals)

    while not open_.empty():
        current_cell = open_.get()[1]

        print(current_cell)     # This should be the go to the square function

        if current_cell in goals:
            break

        for i in range(4):
            child_cell = None
            # This part should be changed to scan the maze and update the walls
            if i == 0:
                if not maze_[0][current_cell[1]][current_cell[0]]:  # Scan for south wall
                    h_walls_[current_cell[1]][current_cell[0]] = 0
                    child_cell = (current_cell[0], current_cell[1]-1)
            elif i == 1:
                if not maze_[0][current_cell[1]+1][current_cell[0]]:    # Scan for north wall
                    h_walls_[current_cell[1]+1][current_cell[0]] = 0
                    child_cell = (current_cell[0], current_cell[1] + 1)
            elif i == 2:
                if not maze_[1][current_cell[1]][current_cell[0]]:  # Scan for east wall
                    v_walls_[current_cell[1]][current_cell[0]] = 0
                    child_cell = (current_cell[0] - 1, current_cell[1])
            else:
                if not maze_[1][current_cell[1]][current_cell[0]+1]:    # Scan for west wall
                    v_walls_[current_cell[1]][current_cell[0]+1] = 0
                    child_cell = (current_cell[0] + 1, current_cell[1])

            if child_cell:
                temp_h_value = h_value(child_cell, goals)
                if temp_h_value < squares[child_cell[1]][child_cell[0]]:
                    squares[child_cell[1]][child_cell[0]] = temp_h_value
                    open_.put((temp_h_value, child_cell))

    return h_walls_, v_walls_


h_walls, v_walls = go_from_to((0, 0), goals_, h_walls, v_walls, maze)
h_walls, v_walls = go_from_to((6, 6), ((0, 0), ), h_walls, v_walls, maze)

print("Horizontal walls")
for i in h_walls:
    print(i)

print("Vertical walls")
for j in v_walls:
    print(j)
