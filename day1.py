def is_valid_sudoku(board):
    # Qatorlarni tekshirish
    for row in range(9):
        seen = set()
        for col in range(9):
            val = board[row][col]
            if val == ".": continue
            if val in seen: return False
            seen.add(val)

    # Ustunlarni tekshirish
    for col in range(9):
        seen = set()
        for row in range(9):
            val = board[row][col]
            if val == ".": continue
            if val in seen: return False
            seen.add(val)

    # 3x3 kvadratlarni tekshirish
    for r in range(0, 9, 3): 
        for c in range(0, 9, 3):
            seen = set()
            for i in range(3):
                for j in range(3):
                    val = board[r + i][c + j]
                    if val == ".": continue
                    if val in seen: return False
                    seen.add(val)
    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                return (i, j)
    return None

def solve(board):
    find = find_empty(board)
    if not find:
        return True 
    row, col = find

    for num in map(str, range(1, 10)):
        board[row][col] = num
        
        if is_valid_sudoku(board):
            if solve(board):
                return True
        
        # Backtracking - noto'g'ri bo'lsa orqaga qaytish
        board[row][col] = "."

    return False

# 1. Jadvalni aniqlash
sudoku_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6",".",],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

# 2. Ishga tushirish
print("Yechilmoqda...")
if solve(sudoku_board):
    print("\nSudoku muvaffaqiyatli yechildi:\n")
    for row in sudoku_board:
        print(" ".join(row))
else:
    print("Yechim topilmadi.")

