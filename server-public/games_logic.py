import random
from constants import *
from logger import logger


class GameLogic:
    def __init__(self, player1, player2):
        """
        Initialize the Tic Tac Toe game with two players.

        Args:
        player1 (dict): Dictionary containing player1's information, including 'id'.
        player2 (dict): Dictionary containing player2's information, including 'id'.
        """
        # Initialize player IDs and starting turn
        self.player1_id = player1["id"]
        self.player2_id = player2["id"]
        # Randomly select who starts
        self.turn_id = random.choice([self.player1_id, self.player2_id])

        self.init_game()

        self.board = [[None for _ in range(self.cols)]
                      for _ in range(self.rows)]

    def validate(self, id, move):

        if not self.turn_id == id:
            return False, "Not your turn!"

        if not self.make_move(move, False):
            return False, "Invalid move!"

        return True, None

    def move(self, to):

        to = self.make_move(to)

        # Prepare response
        r = {}
        r["moved"] = {
            "who": self.turn_id,
            "to": to,
            "turn_string": self.turn_string,

        }

        game_over = self.is_game_over(self.turn_id)

        self.switch_turn()

        r["moved"]["turn_id"] = self.turn_id

        return game_over, r

    def get_turn_id(self):

        return self.turn_id

    def is_game_over(self, player):
        """Check if there is a winning sequence"""
        # Check rows
        for row in range(self.rows):
            for col in range(self.cols - self.win_condition + 1):

                if all(self.board[row][col + i] == player for i in range(self.win_condition)):

                    return {"winner_id": player, "indices": [(row, col+i) for i in range(self.win_condition)], "tie": False}

        # Check columns
        for col in range(self.cols):
            for row in range(self.rows - self.win_condition + 1):
                if all(self.board[row + i][col] == player for i in range(self.win_condition)):
                    return {"winner_id": player, "indices": [(row+i, col) for i in range(self.win_condition)], "tie": False}

        # Check diagonal (top-left to bottom-right)
        for row in range(self.rows - self.win_condition + 1):
            for col in range(self.cols - self.win_condition + 1):
                if all(self.board[row + i][col + i] == player for i in range(self.win_condition)):
                    return {"winner_id": player, "indices": [(row+i, col+i) for i in range(self.win_condition)], "tie": False}

        # Check diagonal (top-right to bottom-left)
        for row in range(self.rows - self.win_condition + 1):
            for col in range(self.win_condition - 1, self.cols):
                if all(self.board[row + i][col - i] == player for i in range(self.win_condition)):
                    return {"winner_id": player, "indices": [(row+i, col-i) for i in range(self.win_condition)], "tie": False}

        # Tie match
        if self.is_full():
            return {"winner_id": None, "indices": None, "tie": True}

        return False

    def is_full(self):
        """Check if the board is full."""
        return all(self.board[i][j] != None for i in range(self.rows) for j in range(self.cols))


# Class to handle the logic for Tic Tac Toe
class TTTLogic(GameLogic):

    def __init__(self, player1, player2):
        super().__init__(player1, player2)

    def init_game(self):
        self.turn_string = "X"  # 'X' starts first
        self.X_id = self.turn_id
        self.O_id = self.player1_id if self.X_id == self.player2_id else self.player2_id

        # Board setup
        self.rows = tic_tac_toe_rows
        self.cols = tic_tac_toe_cols

        self.win_condition = min(self.rows, self.cols)

    def switch_turn(self):
        # Switch turns
        if self.turn_string == "X":
            self.turn_string = "O"
            self.turn_id = self.O_id
        else:
            self.turn_string = "X"
            self.turn_id = self.X_id

    def make_move(self, to, place=True):
        if self.board[to[0]][to[1]] is None:
            if place:
                # Place the move
                self.board[to[0]][to[1]] = self.turn_id
            return to

        return False

    def get_identification_dict(self):

        return {self.X_id: "X", self.O_id: "O", "player1": self.player1_id, "player2": self.player2_id}


# Class to handle the logic for Connect4
class ConnectLogic(GameLogic):
    def __init__(self, player1, player2):
        super().__init__(player1, player2)

    def init_game(self):
        self.turn_string = "red"  # 'red' starts first
        self.red_id = self.turn_id
        self.blue_id = (
            self.player1_id if self.red_id == self.player2_id else self.player2_id
        )

        # Board setup
        self.rows = connect4_rows
        self.cols = connect4_cols

        self.win_condition = connect4_number

    def get_identification_dict(self):

        return {self.red_id: "red", self.blue_id: "blue", "player1": self.player1_id, "player2": self.player2_id}

    def make_move(self, col, place=True):
        # Place a piece in the lowest available row for the specified column
        for r in range(self.rows - 1, -1, -1):
            if self.board[r][col] is None:
                if place:
                    self.board[r][col] = self.turn_id
                return (r, col)
        else:
            return False

    def switch_turn(self):
        # Switch turns
        if self.turn_string == "red":
            self.turn_string = "blue"
            self.turn_id = self.blue_id
        else:
            self.turn_string = "red"
            self.turn_id = self.red_id
