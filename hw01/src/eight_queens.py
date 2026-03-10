def solve_n_queens(n: int) -> list[list[str]]:
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    col = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == n:
            solution = [''.join(r) for r in board]
            result.append(solution)
            return
        for c in range(n):
            if c not in col and (row - c) not in diag1 and (row + c) not in diag2:
                board[row][c] = 'Q'
                col.add(c)
                diag1.add(row - c)
                diag2.add(row + c)
                backtrack(row + 1)
                board[row][c] = '.'
                col.remove(c)
                diag1.remove(row - c)
                diag2.remove(row + c)

    backtrack(0)
    return result

def count_n_queens(n: int) -> int:
    return len(solve_n_queens(n))

if __name__ == "__main__":
    print("8 皇后问题解的数量：", count_n_queens(8))
