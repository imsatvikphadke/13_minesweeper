from board import Board
from board import Board, DIFFICULTIES

class Minesweeper:
     def __init__(self, difficulty="easy"):
        rows, cols, mines = DIFFICULTIES[difficulty]
        self.board = Board(rows, cols, mines)

     def display(self, reveal_mines=False):
        b = self.board
        print("\n   " + " ".join(str(c + 1) for c in range(b.cols)))
        for r in range(b.rows):
            cells = []
            for c in range(b.cols):
                pos = (r, c)
                if reveal_mines and pos in b.mines:
                    ch = "*"
                elif pos in b.flags:
                    ch = "F"
                elif pos not in b.revealed:
                    ch = "#"
                elif pos in b.mines:
                    ch = "*"
                else:
                    ch = str(b.adjacent_mines(r, c))
                cells.append(ch)
            print(f"{r + 1:2} " + " ".join(cells))

    def run(self):
        print("Minesweeper")
        print("Select difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        while True:
            choice = input("> ").strip()
            if choice == "1":
                difficulty = "easy"
                break
            elif choice == "2":
                difficulty = "medium"
                break
            elif choice == "3":
                difficulty = "hard"
                break
            else:
                print("Choose 1, 2, or 3.")
        rows, cols, mines = DIFFICULTIES[difficulty]
        self.board = Board(rows, cols, mines)
        print("Commands: r row col | f row col | q")
        while True:
            self.display()
            raw = input("> ").strip().lower()
            if raw == "q":
                return
            parts = raw.split()
            if len(parts) != 3 or parts[0] not in {"r", "f"}:
                print("Use r row col or f row col.")
                continue
            try:
                r, c = int(parts[1]) - 1, int(parts[2]) - 1
            except ValueError:
                print("Coordinates must be numbers.")
                continue
                 
            if not self.board.in_bounds(r, c):
                print("Outside the board.")
                continue

            if parts[0] == "f":
                self.board.toggle_flag((r, c))
                continue

            if self.board.reveal((r, c)):
               self.display(reveal_mines=True)
               print("BOOM! You hit a mine.")
               return
          
            print("Cell revealed.")
          
            if self.board.won():
                   self.display()
                   print("You cleared the board!")
                   return
