class TicTacToe:
    def __init__(self):
        
        self.board:list[list[int]] = [
           [0,  0,  0],
           [0,  0,  0],
           [0,  0,  0]
        ] # 0 is untaken, 1 is player1, 2 is player2
        
        self.char_map:list[str] = ["-", "X", "O"]
        
        self.player1_turn = True # True => player1, False => player2
        
        
    def display(self) -> None:
        """ Display the board """
        for row in self.board:
            for pos in row:
                print(
                    self.char_map[pos],
                    end=""
                )
                print("  ", end="")
            print()
            
    def turn(self) -> None:
        """ Allow player to enter their position """
        
        print(f"*** {'Player 1' if self.player1_turn else 'Player 2'} ({self.char_map[1] if self.player1_turn else self.char_map[2]}) take your turn ***")
        while True:
            row = input("Enter row (1-3)\n>> ")
            col = input("Enter column (1-3)\n>> ")
            
            try:
                row = int(row) - 1 
                col = int(col) - 1

                if (
                    row >= 0 and row <= 2 and
                    col >= 0 and col <= 2 and
                    self.board[row][col] == 0
                ): break
            except: ...
            
        # Update the board state
        self.board[row][col] = 1 if self.player1_turn else 2
    
        self.player1_turn = not self.player1_turn
        
    def evaluate(self) -> bool:
        # Wins buy full rows / full columns
        for i in range(len(self.board)):
            if (
                ((self.board[0][i] == self.board[1][i] and
                self.board[1][i] == self.board[2][i]) or 
                (self.board[i][0] == self.board[i][1] and
                self.board[i][1] == self.board[i][2])) and
                self.board[i][i] != 0
            ): return self.conclude(self.board[i][i] == 1)
        
        # Diagonals
        if (
            (self.board[0][0] == self.board[1][1] and
            self.board[1][1] == self.board[2][2]) or
            (self.board[0][0] == self.board[1][1] and
            self.board[1][1] == self.board[2][2]) and
            self.board[i][i] != 0
        ): return self.conclude(self.board[i][i] == 1)
    
        return False
                
    def conclude(self, is_player1:bool) -> bool:
        print(f"*** {'Player 1' if is_player1 else 'Player 2'} ({self.char_map[1] if is_player1 else self.char_map[2]}) Wins! ***")
        return True