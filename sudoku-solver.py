input = [0, 0, 8,   0, 0, 0,   0, 0, 0,
         4, 0, 0,   6, 0, 0,   0, 0, 9,
         5, 0, 0,   4, 1, 0,   0, 3, 0,

         0, 0, 0,   0, 0, 0,   2, 0, 0,
         0, 0, 3,   0, 0, 0,   0, 0, 0,
         0, 0, 2,   0, 4, 0,   5, 0, 0,

         6, 0, 0,   0, 0, 2,   0, 0, 8,
         0, 0, 0,   7, 0, 0,   1, 0, 0,
         0, 1, 0,   0, 8, 6,   0, 0, 2]


def get_digit(input, i):
    return 0


def get_digits_in_square(input, i):
    return []


def get_digits_in_row(input, i):
    return []


def get_digits_in_column(input, i):
    return []


def big_union(list_of_lists):
    return []


def one_minus(digit_list):
    return []


def get_possible_digits(input, i):
    square_digits = get_digits_in_square(input, i)
    row_digits = get_digits_in_row(input, i)
    column_digits = get_digits_in_column(input, i)
    invalid_digits = big_union([square_digits, row_digits, column_digits])
    valid_digits = one_minus(invalid_digits)
    return valid_digits


def get_all_possible_digits(input):
    map_of_possible_digits = []
    for i in range(len(input)):
        possible_digits = get_possible_digits(input, i)
        if len(possible_digits) == 0:
            pass    # TODO: handle this later
        elif len(possible_digits) == 1:
            input[i] = possible_digits[0]
        else:
            map_of_possible_digits = possible_digits
    if map_of_possible_digits:
        get_all_possible_digits()


get_all_possible_digits(input)