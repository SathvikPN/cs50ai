"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # raise NotImplementedError

    # Given: In the initial game state, X gets the first move.
    moves = 0
    for row in board:
        for cell in row:
            if cell == X or cell == O:
                moves += 1
    # odd nos of moves already happened
    if moves & 1:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError
    action_set = set()
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == EMPTY:
                action_set.add((y, x))
    return action_set


def inbound(y, x):
    return 0 <= y <= 2 and 0 <= x <= 2


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError

    if action is None:
        raise Exception("Action cannot be None")
    new_board = copy.deepcopy(board)
    y, x = action[0], action[1]
    if new_board[y][x] != EMPTY or not inbound(y, x):
        raise Exception("invalid action on the board state")

    new_board[y][x] = player(board=board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError
    # Check rows and columns
    for i in range(3):
        # Check row
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        # Check column
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError
    if winner(board=board):
        return True

    empty_cells = 0
    for row in board:
        for x in row:
            if x == EMPTY:
                empty_cells += 1

    if empty_cells == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # raise NotImplementedError
    winning_player = winner(board=board)
    if winning_player == X:
        return 1

    if winning_player == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board=board):
        return None

    current_player = player(board=board)
    if current_player == X:
        # wants board_score to maxx out to 1
        max_score = -1
        best_action = None
        for action in actions(board=board):
            new_board = result(board=board, action=action)
            score = minimax_value(new_board)
            if score > max_score:
                best_action = action
                max_score = score
                if max_score == 1:
                    break
        return best_action

    if current_player == O:
        # wants board_score to min
        min_score = 1
        best_action = None
        for action in actions(board=board):
            new_board = result(board=board, action=action)
            score = minimax_value(new_board)
            if score < min_score:
                best_action = action
                min_score = score
                if min_score == -1:
                    break
        return best_action


def minimax_value(board):
    if terminal(board=board):
        return utility(board=board)

    current_player = player(board=board)
    if current_player == X:
        max_value = -1  # states: -1, 0 , 1
        for action in actions(board=board):
            new_board = result(board=board, action=action)
            max_value = max(max_value, minimax_value(new_board))
            if max_value == 1:
                return 1
        return max_value

    if current_player == O:
        min_value = 1
        for action in actions(board=board):
            new_board = result(board=board, action=action)
            min_value = min(min_value, minimax_value(new_board))
            if min_value == -1:
                return -1
        return min_value
