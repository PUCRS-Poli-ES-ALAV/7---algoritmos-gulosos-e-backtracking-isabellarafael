
from typing import Any, List, NewType

try:
    async def __ignore() -> bool | None: ...
except:
    print('Needs Python 3.10 or higher')
    exit(1)

BoardType = NewType('BoardType', List[List[Any]])
QueenType = NewType('QueenType', Any)


def is_valid_pos(board: BoardType, n: int, x: int, y: int, queen: QueenType = 'Q') -> bool:
    def intersects_with_queen(board: BoardType, x: int, y: int, queen: QueenType) -> bool:
        try:
            if board[x][y] == queen:
                return True
        except:
            pass
        return False

    # Line
    for i in range(n):
        if intersects_with_queen(board, x, i, queen):
            return False

    # Column
    for i in range(n):
        if intersects_with_queen(board, i, y, queen):
            return False

    i, j = x - 1, y - 1
    while i >= 0 and j >= 0:
        if intersects_with_queen(board, i, j, queen):
            return False
        i -= 1
        j -= 1

    i, j = x + 1, y + 1
    while i < n and j < n:
        if intersects_with_queen(board, i, j, queen):
            return False
        i += 1
        j += 1

    i, j = x - 1, y + 1
    while i >= 0 and j < n:
        if intersects_with_queen(board, i, j, queen):
            return False
        i -= 1
        j += 1

    i, j = x + 1, y - 1
    while i < n and j >= 0:
        if intersects_with_queen(board, i, j, queen):
            return False
        i += 1
        j -= 1

    return True


def print_board(board: BoardType) -> None:
    print()
    for l in board:
        print(' ', *l)
    print()


def create_board(n: int) -> BoardType:
    return BoardType([['-' for _ in range(n)] for _ in range(n)])


def n_queens(n: int, x: int, y: int, queen: QueenType = 'Q', _print_board: bool = True) -> BoardType | None:
    board = create_board(n)

    if is_valid_pos(board, n, x, y, queen):
        board[x][y] = queen

    for i in range(n):
        for j in range(n):
            if is_valid_pos(board, n, i, j, queen):
                board[i][j] = queen

    if _print_board:
        print_board(board)

    if sum(map(lambda p: p.count(queen), board)) == n:
        return board
    return None


n = 4
queen = 'Q'
solutions = set()
for i in range(n):
    for j in range(n):
        if (board := n_queens(n, i, j, queen, False)) is None or \
           (board_hash := hash(''.join([p for l in board for p in l]))) in solutions:
            continue
        solutions.add(board_hash)
        print_board(board)


# def n_queens_backtracking(board: BoardType, n: int, x: int, y: int, queen: QueenType = 'Q') -> BoardType:
#     if is_valid_pos(board, n, x, y, queen):
#         board[x][y] = queen

#     x += 1
#     if x >= n:
#         x = 0
#         y += 1

#     if y >= n:
#         return board
#     else:
#         return n_queens_backtracking(board, n, x, y, queen)

# print_board(n_queens_backtracking(create_board(n), n, 0, 0, queen))
# n = 10
# queen = 'Q'
# solutions: List[BoardType] = []
# for i in range(n):
#     for j in range(n):
#         board = n_queens(n, i, j, queen, _print_board=False)
#         board_hash = hash_board(board)
#         solutions.append(board)
#         print(' ' * 30)
#         print_board(board)
#         print(' ' * 30)

# def n_queens_backtrack(n: int, queen: QueenType = 'Q') -> List[BoardType]:
#     solutions: List[BoardType] = []
#     def backtrack(board: BoardType, n: int, queen: QueenType, x: int, y: int) -> BoardType:
#         if is_valid_pos(board, n, x, y):
#             board[x][y] = queen
#         for i in range(n):
#             for j in range(n):
#                 return backtrack(board, n, queen, i, j)
#         return board
#     # board = create_board(n)
#     for j in range(n):
#         for i in range(n):
#             board = create_board(n)
#             solutions.append(backtrack(board, n, queen, i, j))
#     for b in solutions:
#         print_board(b)
#         print('-------------------')
#     return solutions

# n_queens(n=7, x=4, y=4, queen='Q')
# n_queens_backtrack(n=7)
