def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Linhas
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    # Colunas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    # Diagonais
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def main():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    for turn in range(9):
        print_board(board)
        row = int(input(f"Jogador {player}, escolha a linha (0-2): "))
        col = int(input(f"Jogador {player}, escolha a coluna (0-2): "))
        if board[row][col] == " ":
            board[row][col] = player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Jogador {winner} ganhou!")
                return
            player = "O" if player == "X" else "X"
        else:
            print("Posição indisponível, tente novamente.")
    print_board(board)
    print("Empate!")

if __name__ == "__main__":
    main()

