class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = {k:set() for k in range(len(board))}
        rows = {k:set() for k in range(len(board))}
        cells = {}
        # init 
        for r in range(9):
            rows[r] = set()
            for c in range(9):
                columns[c] = set()
                cells[(r,c)] = set()
                

        # scan
        for r in range(9):
            for c in range(9):
                current_square = board[r][c]
                if current_square == ".":
                    continue
                

                if current_square in columns[c]:
                    print("Number exists in column")
                    return False
                if current_square in rows[r]:
                    print("Number exists in row")
                    return False
                if current_square in cells[(r // 3,c //3 )]:
                    print("Number exists in cell")
                    return False
                
                # add to seen for each
                columns[c].add(current_square)
                rows[r].add(current_square)
                cells[(r // 3,c // 3)].add(current_square)
                # print("row: {}, column: {}".format(r,c))
                # print("columns: {}".format(columns))
                # print("rows: {}".format(rows))
                print("cells: {}".format(cells))
        
        return True