from queue import PriorityQueue

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

squares = [[[float('inf'), float('inf')] for i in range(14)] for j in range(14)]
goals = ((6, 6), (7, 6), (6, 7), (7, 7))


def go_to(current_cell, target_cell, path):
    forward_path = [target_cell]
    if path is not None:
        while target_cell != current_cell:
            target_cell = path[target_cell]
            forward_path.append(target_cell)
    forward_path = forward_path[::-1]
    return forward_path


def go_to_target(target_cell, current_cell, path, start=(0, 0)):

    path_from_target = [target_cell]
    if path is not None:
        while target_cell != start and target_cell != current_cell:
            target_cell = path[target_cell]
            path_from_target.append(target_cell)

        path_from_current = [current_cell]
        while current_cell not in path_from_target and current_cell != start:
            current_cell = path[current_cell]
            path_from_current.append(current_cell)
        else:
            index_ = path_from_target.index(current_cell)
            path_from_target = path_from_target[:index_]
            path_from_target += path_from_current[::-1]
        return path_from_target[::-1][1:]


def h_value(cell):
    return min(abs(goals[0][0]-cell[0]+goals[0][1]-cell[1]),
               abs(goals[1][0]-cell[0]+goals[1][1]-cell[1]),
               abs(goals[2][0]-cell[0]+goals[2][1]-cell[1]),
               abs(goals[3][0]-cell[0]+goals[3][1]-cell[1]))


def g_value(cell, start):
    return abs(cell[0] - start[0]) + abs(cell[1] - start[1])


def a_star(horizontal_walls_, vertical_walls_, start=(0, 0)):
    # temporary variable cells:
    cells = 0

    open_ = PriorityQueue()
    open_.put((h_value(start), h_value(start), start))
    squares[start[0]][start[1]][0], squares[start[0]][start[1]][1] = h_value(start), h_value(start)
    path = {}
    search_path = []
    current_cell = start

    while not open_.empty():
        prev_cell = current_cell
        current_cell = open_.get()[2]
        go_path = go_to_target(current_cell, prev_cell, path, start)
        # Printing the going path
        for i in go_path:
            cells += 1
            print(i)

        search_path.append(current_cell)
        if current_cell in goals:
            break

        for i in range(4):
            child_cell = None
            match i:
                case 0:
                    if not horizontal_walls_[current_cell[1]][current_cell[0]]:
                        child_cell = (current_cell[0], current_cell[1]-1)
                case 1:
                    if not horizontal_walls_[current_cell[1]+1][current_cell[0]]:
                        child_cell = (current_cell[0], current_cell[1]+1)
                case 2:
                    if not vertical_walls_[current_cell[1]][current_cell[0]]:
                        child_cell = (current_cell[0]-1, current_cell[1])
                case 3:
                    if not vertical_walls_[current_cell[1]][current_cell[0]+1]:
                        child_cell = (current_cell[0]+1, current_cell[1])

            if child_cell:
                temp_g_score = g_value(current_cell, start) + 1
                temp_f_score = temp_g_score + h_value(child_cell)

                if temp_f_score < squares[child_cell[0]][child_cell[1]][0]:
                    if (path.get(current_cell) and path[current_cell] != child_cell) or not path.get(current_cell):
                        path[child_cell] = current_cell
                        squares[child_cell[0]][child_cell[1]][0] = temp_f_score
                        squares[child_cell[0]][child_cell[1]][1] = temp_g_score
                        open_.put((temp_f_score, h_value(child_cell), child_cell))

    forward_path = go_to(start, current_cell, path)
    # while current_cell != start:
    #     print(f"{current_cell[0]}, {current_cell[1]}")
    #     forward_path[path[current_cell]] = current_cell
    #     current_cell = path[current_cell]
    print(cells)
    return search_path, path, forward_path


search_path_, path_, forward_path_ = a_star(horizontal_walls, vertical_walls)
print("Search path")
for element in search_path_:
    print(element, end=" ")

print("\npath")
print(path_)

print("\nforward path")
for element in forward_path_:
    print(element, end=" ")
