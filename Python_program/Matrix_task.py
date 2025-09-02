# choose your position in 3X3 matrix put the 'X' sign 

Matrix = [[1,1,1],[1,1,1],[1,1,1]]
print(Matrix)
Position = input("Enter the Position where you want to put X mark: ")

row_number = int(Position[0])
column_number = int(Position[1])

if row_number > 0 and row_number <= len(Matrix):
    column_size = len(Matrix[row_number-1])
    if column_number > 0 and column_number <= column_size:
        Matrix[row_number-1][column_number-1] = "X"
        print(Matrix)
    else:
        print('Index Out OF Range Put Right Column Value')
else:
    print('Index Out OF Range Put Right Row Value')


