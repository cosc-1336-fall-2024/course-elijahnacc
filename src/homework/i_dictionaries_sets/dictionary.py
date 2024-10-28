
def get_p_distance(list1, list2):

    # For Loop iterates through parameters : Accumulates distance when given index of lists is !=
    
    distance = 0

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            distance += 0.1
    
    return distance

def get_p_distance_matrix(list1, grid_size):

    # Matrix is defined by [] : For Loop appends brackets and 0 values by Grid Size
    # Nested For Loop iterates through rows and columns of the nested list matrix
    # If P Distance is not 0.0 for given index : Runs function to get distance and assigns to matrix at index

    matrix = []
    for row in range(grid_size):
        matrix.append([])
        for col in range(grid_size):
            matrix[row].append(0.00000)

    for row in range(len(list1)):
        for col in range(len(list1)):
            if list1[row] != list1[col]:
                matrix[row][col] = round(get_p_distance(list1[row], list1[col]), 5)

    return matrix