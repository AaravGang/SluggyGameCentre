# Kinda a hack, but since I'm sending over an object from the server
# just making this file to avoid errors
import math
from logger import logger
import random


class TTTLogic:
    pass


class ConnectLogic:
    pass


class BoardGame:
    def __init__(self, game_id, ai, human, turn, make_move_req, rows=3, cols=3, win_condition=3, connect=False):

        self.game_id = game_id
        self.rows = rows
        self.cols = cols
        self.win_condition = win_condition
        self.connect = connect
        self.EMPTY = ' '
        self.board = [[self.EMPTY for _ in range(cols)] for _ in range(rows)]
        self.ai = ai  # AI
        self.human = human  # Human
        self.turn = turn

        self.make_move_req = make_move_req

        # If it is AI's turn to start
        if self.turn == self.ai:
            self.first_move()

    def first_move(self):
        if self.connect:
            return self.make_move_req(
                self.game_id, self.cols//2+1)

        return self.find_and_place_best_move()

    def print_board(self):
        """Print the current state of the board."""
        for row in self.board:
            print('|'.join(row))
            print('-' * (2 * self.cols - 1))

    def is_winner(self, player):
        """Check if there is a winning sequence"""
        # Check rows
        for row in range(self.rows):
            for col in range(self.cols - self.win_condition + 1):
                if all(self.board[row][col + i] == player for i in range(self.win_condition)):
                    return True

        # Check columns
        for col in range(self.cols):
            for row in range(self.rows - self.win_condition + 1):
                if all(self.board[row + i][col] == player for i in range(self.win_condition)):
                    return True

        # Check diagonal (top-left to bottom-right)
        for row in range(self.rows - self.win_condition + 1):
            for col in range(self.cols - self.win_condition + 1):
                if all(self.board[row + i][col + i] == player for i in range(self.win_condition)):
                    return True

        # Check diagonal (top-right to bottom-left)
        for row in range(self.rows - self.win_condition + 1):
            for col in range(self.win_condition - 1, self.cols):
                if all(self.board[row + i][col - i] == player for i in range(self.win_condition)):
                    return True

        return False

    def is_full(self):
        """Check if the board is full."""
        return all(self.board[i][j] != self.EMPTY for i in range(self.rows) for j in range(self.cols))

    def evaluate(self):
        """Evaluate the board state."""
        if self.is_winner(self.ai):
            return 1  # AI wins
        elif self.is_winner(self.human):
            return -1  # Human wins
        return 0  # Draw

    def minimax(self, depth, alpha, beta, is_maximizing):
        """Minimax with alpha beta pruning."""
        score = self.evaluate()

        # Base cases: win, lose, or draw
        if abs(score) > 0 or self.is_full():
            return score

        if depth == 0:  # Limit search depth for efficiency
            return score

        if is_maximizing:
            best_score = -math.inf
            for col in range(self.cols):
                for row in range(self.rows-1, -1, -1):
                    if self.board[row][col] == self.EMPTY:
                        self.board[row][col] = self.ai  # AI move
                        score = self.minimax(depth - 1, alpha, beta, False)
                        self.board[row][col] = self.EMPTY  # Undo move
                        best_score = max(best_score, score)

                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break

            return best_score

        else:
            best_score = math.inf
            for col in range(self.cols):
                for row in range(self.rows-1, -1, -1):
                    if self.board[row][col] == self.EMPTY:
                        self.board[row][col] = self.human  # Human move
                        score = self.minimax(depth - 1, alpha, beta, True)
                        self.board[row][col] = self.EMPTY  # Undo move
                        best_score = min(best_score, score)

                        beta = min(beta, score)
                        if beta <= alpha:
                            break

            return best_score

    def find_and_place_best_move(self, depth=4):
        """Find the best move."""
        best_value = -math.inf
        best_move = [-1, -1]
        for col in range(self.cols):
            for row in range(self.rows-1, -1, -1):
                if self.board[row][col] == self.EMPTY:

                    self.board[row][col] = self.ai  # AI move
                    move_value = self.minimax(
                        depth - 1, -math.inf, math.inf, False)

                    self.board[row][col] = self.EMPTY  # Undo move

                    # logger.info(f"{best_value},{move_value}")
                    if move_value > best_value:
                        best_value = move_value
                        best_move = [row, col]

                    if self.connect:
                        break

        self.make_move_req(
            self.game_id, best_move[1] if self.connect else best_move)

        return best_move

    def make_move(self, row, col, player):
        """Make a move on the board. In Connect 4, moves follow gravity."""
        if self.connect:
            # For Connect 4, move to the lowest possible row in the column
            for i in range(self.rows - 1, -1, -1):
                if self.board[i][col] == self.EMPTY:
                    self.board[i][col] = player
                    break

        else:
            # For Tic-Tac-Toe
            if self.board[row][col] == self.EMPTY:
                self.board[row][col] = player

        self.turn = self.ai if player == self.human else self.human

        # if it's the ai's turn make the best move
        if self.turn == self.ai:
            self.find_and_place_best_move()

    def game_over_protocol(self, indices, winner_id, *args):
        """Handle end-of-game protocol."""
        logger.debug(f"[BOT]: GAME OVER {winner_id} won!")
