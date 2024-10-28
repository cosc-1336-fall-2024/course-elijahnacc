from dictionary import get_p_distance_matrix

def main():

    selection = 0

    while selection != 2:

        print("MENU\n1 - Get P Distance Matrix\n2 - Exit")
        selection = int(input('Please enter menu selection: '))

        if selection == 1:

            grid_size = int(input('Enter number of strands: '))
            strand_list = [[0 for j in range(10)]for i in range(4)]
            temp_list = []

            for i in range(grid_size):
                while True:
                    
                    strand = ''
                    
                    while len(strand) != 10:
                        strand = str(input(f'Enter strand {i+1}: '))
                        if len(strand) == 10:
                            break
                        print('Strand must be 10 characters')

                    strand = strand.upper()
                    for j in range(10):
                        strand_list[i][j] = strand[j]

                    break

            matrix = get_p_distance_matrix(strand_list, grid_size)
            print(matrix)
            exit()

if __name__ == '__main__':
    main()