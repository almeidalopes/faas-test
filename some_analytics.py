import numpy as np

# main_table = list(list())

# main_table = np.array([[7, 0, 0, 5, 3, 8, 9, 0, 0],
#                        [0, 0, 0, 0, 0, 7, 0, 3, 0],
#                        [0, 0, 0, 1, 0, 0, 0, 0, 4],
#                        [8, 0, 9, 0, 0, 2, 0, 5, 3],
#                        [3, 0, 0, 0, 0, 0, 0, 0, 6],
#                        [6, 5, 0, 3, 0, 0, 4, 0, 8],
#                        [1, 0, 0, 0, 0, 3, 0, 0, 0],
#                        [0, 6, 0, 4, 0, 0, 0, 0, 0],
#                        [0, 0, 3, 6, 2, 1, 0, 0, 7]])
#
# main_table = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
#                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                        [0, 0, 0, 0, 0, 0, 0, 0, 0]])
#
# main_table = np.array([[0, 8, 0, 0, 0, 0, 0, 2, 0],
#                        [0, 0, 2, 0, 9, 0, 7, 0, 0],
#                        [6, 0, 0, 0, 8, 0, 0, 0, 1],
#                        [1, 0, 0, 3, 4, 8, 0, 0, 2],
#                        [0, 9, 6, 2, 0, 1, 8, 3, 0],
#                        [8, 0, 0, 6, 7, 9, 0, 0, 5],
#                        [9, 0, 0, 0, 2, 0, 0, 0, 8],
#                        [0, 0, 8, 0, 1, 0, 3, 0, 0],
#                        [0, 4, 0, 0, 0, 0, 0, 1, 0]])
# main_table = np.array([[7, 0, 9, 1, 0, 0, 0, 0, 8],
#                        [0, 0, 4, 0, 0, 6, 0, 0, 0],
#                        [0, 0, 0, 4, 0, 0, 0, 3, 5],
#                        [0, 9, 0, 0, 7, 0, 3, 0, 4],
#                        [0, 0, 0, 8, 0, 1, 0, 0, 0],
#                        [5, 0, 8, 0, 3, 0, 0, 2, 0],
#                        [8, 3, 0, 0, 0, 5, 0, 0, 0],
#                        [0, 0, 0, 2, 0, 0, 6, 0, 0],
#                        [1, 0, 0, 0, 0, 7, 8, 0, 9]])
main_table = np.array([[0, 0, 0, 9, 0, 0, 4, 0, 0],
                       [0, 7, 1, 0, 6, 0, 0, 0, 3],
                       [0, 0, 0, 0, 0, 8, 5, 0, 9],
                       [0, 0, 5, 0, 8, 0, 0, 0, 4],
                       [7, 0, 2, 0, 0, 0, 1, 0, 5],
                       [4, 0, 0, 0, 9, 0, 7, 0, 0],
                       [6, 0, 7, 4, 0, 0, 0, 0, 0],
                       [8, 0, 0, 0, 1, 0, 3, 5, 0],
                       [0, 0, 3, 0, 0, 7, 0, 0, 0]])


def get_first_line_id(quadrant_id):
    return quadrant_id // 3 * 3


def get_first_column_id(quadrant_id):
    return quadrant_id % 3 * 3


def get_quadrant_id(line, column):
    return 3 * (line // 3) + (column // 3)


def get_quadrant(table, line, column):
    quadrant_id = get_quadrant_id(line, column)
    return table[get_first_line_id(quadrant_id):get_first_line_id(quadrant_id) + 3, get_first_column_id(quadrant_id):get_first_column_id(quadrant_id) + 3]


def get_quadrant_numbers(table, quadrant_number):
    quadrant = list()
    for i in range(3):
        for j in range(3):
            quadrant.append(table[i + 3 * (quadrant_number // 3), j + 3 * (quadrant_number % 3)])
    return quadrant


def draw_table(table):
    print('    0 1 2   3 4 5   6 7 8')
    for line in range(9):
        if line % 3 == 0:
            print('  ' + '-' * 25)
        print(str(line) + ' | ' + ' '.join(map(str, table[line, 0:3])) + ' | ' + ' '.join(
            map(str, table[line, 3:6])) + ' | ' + ' '.join(map(str, table[line, 6:9])) + ' | ' + str(line))
    print('  ' + '-' * 25)
    print('    0 1 2   3 4 5   6 7 8')


def evaluate_busy_neighborhood(mode, table, line, column):
    assert mode in ['line', 'column']
    busy = True
    if mode == 'line':
        for i in range(3):
            if (i != column % 3) and (table[line, i + get_first_column_id(get_quadrant_id(line, column))] == 0):
                busy = False
                break
    elif mode == 'column':
        for j in range(3):
            if (j != line % 3) and (table[j + get_first_line_id(get_quadrant_id(line, column)), column] == 0):
                busy = False
                break
    return busy


def exist_in_line(table, line, number):
    return number in table[line, :]


def exist_in_column(table, column, number):
    return number in table[:, column]


def exist_in_quadrant(table, quadrant_number, number):
    return number in get_quadrant_numbers(table, quadrant_number)


def check_position(table, line, column, number):
    working_quadrant = get_quadrant(table, line, column)
    working_quadrant = working_quadrant != 0
    quadrant_number = get_quadrant_id(line, column)
    # print('Quadrant is ' + str(quadrant_number))
    if exist_in_quadrant(table, quadrant_number, number):
        # print('Number aready exists in this quadrant!')
        return False
    # print('- Checking number ' + str(number) + ' in [' + str(line) + ', ' + str(column) + ']')
    # print('---- Checking line ' + str(get_first_line_id(quadrant_number)) + ' to ' + str(get_first_line_id(quadrant_number) + 2))
    for i in range(get_first_line_id(quadrant_number), get_first_line_id(quadrant_number) + 3):
        # print('------ Checking line ' + str(i))
        if exist_in_line(table, i, number):
            working_quadrant[i % 3, :] = True
    # print('---- Checking column ' + str(get_first_column_id(quadrant_number)) + ' to ' + str(get_first_column_id(quadrant_number) + 2))
    for j in range(get_first_column_id(quadrant_number), get_first_column_id(quadrant_number) + 3):
        # print('------ Checking column ' + str(j))
        if exist_in_column(table, j, number):
            working_quadrant[:, j % 3] = True
    working_quadrant[line % 3, column % 3] = False
    if (np.count_nonzero(working_quadrant) == 8) or check_last_number(table, line, column, number):
        return True
    else:
        return False


def check_column(table, column, number):
    working_list = np.isin(table[:, column], 0)
    for i in np.where(working_list)[0]:
        if exist_in_line(table, i, number) or exist_in_quadrant(table, get_quadrant_id(i, column), number):
            working_list[i] = False
    if np.count_nonzero(working_list) == 1:
        return np.where(working_list)[0][0]
    else:
        return -1


def check_line(table, line, number):
    working_list = np.isin(table[line, :], 0)
    for j in np.where(working_list)[0]:
        if exist_in_column(table, j, number) or exist_in_quadrant(table, get_quadrant_id(line, j), number):
            working_list[j] = False
    if np.count_nonzero(working_list) == 1:
        return np.where(working_list)[0][0]
    else:
        return -1


def check_last_number(table, line, column, number):
    if ((number not in table[line, :]) and (np.count_nonzero(table[line, :]) == 8)) or \
            ((number not in table[:, column]) and (np.count_nonzero(table[:, column]) == 8)) or \
            ((number not in get_quadrant(table, line, column)) and (np.count_nonzero(get_quadrant(table, line, column)) == 8)):
        return True
    else:
        return False


def main():
    draw_table(main_table)
    loop_again = True
    while loop_again:
        loop_again = False
        for number in range(1, 10):
            for i in range(9):
                for j in range(9):
                    # print('Checking number ' + str(number) + ' in [' + str(i) + ', ' + str(j) + '] which is ' + str(main_table[i, j]))
                    if main_table[i, j] == 0:
                        if check_position(main_table, i, j, number):
                            print('\nFound number ' + str(number) + ' in [' + str(i) + ', ' + str(j) + '] !!!\n')
                            main_table[i, j] = number
                            draw_table(main_table)
                            loop_again = True
        if not loop_again:
            for number in range(1, 10):
                for j in range(9):
                    if number not in main_table[:, j]:
                        found_line = check_column(main_table, j, number)
                        if found_line > -1:
                            print('\nFound number ' + str(number) + ' in [' + str(found_line) + ', ' + str(j) + '] !!!2\n')
                            main_table[found_line, j] = number
                            draw_table(main_table)
                            loop_again = True
        if not loop_again:
            for number in range(1, 10):
                for i in range(9):
                    if number not in main_table[i, :]:
                        found_column = check_line(main_table, i, number)
                        if found_column > -1:
                            print('\nFound number ' + str(number) + ' in [' + str(i) + ', ' + str(found_column) + '] !!!2\n')
                            main_table[i, found_column] = number
                            draw_table(main_table)
                            loop_again = True

    print('\nFINAL RESULT:\n')
    draw_table(main_table)
    print(main_table[:, 3] == 0)
    test = main_table[:, 3] == 0
    print(test)
    print(type(test))
    test[5]=False
    test[6] = False


if __name__ == "__main__":
    main()
