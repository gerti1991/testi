
def find_highest_square_matrix(matrix):

    r = len(matrix)
    c = len(matrix[0])

    target = min(r,c)
    row_score = 0
    col_score = 0
    check_col = 0
    square_matrix = []
    temp = []

    while row_score < target and col_score <target:
    
        for i in range(r):
            temp = []
            for j in range(c):            
                if matrix[i][j] == 0:
                    row_score = 0
                    temp = []            
                try:
                    if matrix[i][j+check_col] == 1:
                        row_score += 1
                        temp.append(f"{i};{j+check_col}")
                except IndexError:
                    pass
                if row_score == target:
                    check_col = int(temp[0][-1])
                    col_score +=1                
                    break
            if len(temp)==target:
                square_matrix.append(temp)
            row_score = 0
        if col_score < target:
            col_score = 0
            square_matrix = []
            target -=1

    cor = square_matrix
    square_matrix = []

    for i in range(len(cor)):
        i = []
        square_matrix.append(i)
        for j in range(len(cor[0])):
            i.append(1)


    return f"Best square matrix is {len(cor)} x {len(cor[0])} \nSquared SubMatrix is : {square_matrix} \nCoordinate taken from old matrix {cor}"



matrix = [[0,1,0,1,1],
          [0,1,1,1,0],
          [1,1,1,1,0],
          [1,1,1,1,0],
          [1,1,0,1,1],
          [0,1,0,1,0]
]

print(find_highest_square_matrix(matrix))






