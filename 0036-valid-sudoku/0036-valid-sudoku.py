class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows= {0:[],
           1:[],
           2:[],
           3:[],
           4:[],
           5:[],
           6:[],
           7:[],
           8:[]}

        coulumns= {0:[],
                1:[],
                2:[],
                3:[],
                4:[],
                5:[],
                6:[],
                7:[],
                8:[]}


        cubes= {0:[],
                1:[],
                2:[],
                3:[],
                4:[],
                5:[],
                6:[],
                7:[],
                8:[]}


        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] in rows[row]:
                    return False
                elif board[row][column] not in rows[row] and board[row][column]!=".":
                    rows[row].append(board[row][column])   
                    
                if board[row][column] in coulumns[column]:
                    return False
                elif board[row][column] not in coulumns[column] and board[row][column]!=".":
                    coulumns[column].append(board[row][column])
                    
                if row<3 and column<3 and board[row][column]!=".":
                    if board[row][column] not in cubes[0]:
                        cubes[0].append(board[row][column])
                    else:
                        return False

                elif row<3 and column<6 and board[row][column]!=".":
                    if board[row][column] not in cubes[1]:
                        cubes[1].append(board[row][column])
                    else:
                        return False
                
                elif row<3 and column<9 and board[row][column]!=".":
                    if board[row][column] not in cubes[2]:
                        cubes[2].append(board[row][column])
                    else:
                        return False
                        
                elif row<6 and row>2 and column<3 and board[row][column]!=".":
                    if board[row][column] not in cubes[3]:
                        cubes[3].append(board[row][column])
                    else:
                        return False
                        
                elif row<6 and row>2 and column<6 and board[row][column]!=".":
                    if board[row][column] not in cubes[4]:
                        cubes[4].append(board[row][column])
                    else:
                        return False
                        
                elif row<6 and row>2 and column<9 and board[row][column]!=".":
                    if board[row][column] not in cubes[5]:
                        cubes[5].append(board[row][column])
                    else:
                        return False
                        
                elif row<9 and row>5 and column<3 and board[row][column]!=".":
                    if board[row][column] not in cubes[6]:
                        cubes[6].append(board[row][column])
                    else:
                        return False
                        
                elif row<9 and row>5 and column<6 and board[row][column]!=".":
                    if board[row][column] not in cubes[7]:
                        cubes[7].append(board[row][column])
                    else:
                        return False  
                        
                elif row<9 and row>5 and column<9 and board[row][column]!=".":
                    if board[row][column] not in cubes[8]:
                        cubes[8].append(board[row][column])
                    else:
                        return False 
        return True
    