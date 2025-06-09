import pytest
from tictactoe import player, X, O, EMPTY

# test_tictactoe.py


def test_player_initial_board():
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    assert player(board) == X

def test_player_one_move():
    board = [
        [X, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    assert player(board) == O

def test_player_two_moves():
    board = [
        [X, O, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    assert player(board) == X

def test_player_full_board():
    board = [
        [X, O, X],
        [X, O, O],
        [O, X, X]
    ]
    assert player(board) == O




from tictactoe import actions, result, winner, terminal

def test_actions_initial_state():
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    expected = {(i, j) for i in range(3) for j in range(3)}
    assert actions(board) == expected

def test_actions_partial_board():
    board = [
        [X, O, EMPTY],
        [EMPTY, X, EMPTY],
        [O, EMPTY, EMPTY]
    ]
    expected = {(0,2), (1,0), (1,2), (2,1), (2,2)}
    assert actions(board) == expected

def test_result_valid_move():
    board = [
        [X,     O, EMPTY],
        [EMPTY, X, EMPTY],
        [O, EMPTY, EMPTY]
    ]
    action = (1, 0)
    new_board = result(board, action)
    assert new_board[1][0] == X 
    # Original board should not be mutated
    assert board[1][0] == EMPTY

def test_result_invalid_move():
    board = [
        [X, O, EMPTY],
        [EMPTY, X, EMPTY],
        [O, EMPTY, EMPTY]
    ]
    action = (0, 0)  # Already occupied
    import pytest
    with pytest.raises(Exception):
        result(board, action)

def test_winner_row():
    board = [
        [X, X, X],
        [O, O, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    assert winner(board) == X

def test_winner_column():
    board = [
        [O, X, EMPTY],
        [O, X, EMPTY],
        [O, EMPTY, X]
    ]
    assert winner(board) == O

def test_winner_diagonal():
    board = [
        [X, O, O],
        [EMPTY, X, EMPTY],
        [O, EMPTY, X]
    ]
    assert winner(board) == X

def test_winner_none():
    board = [
        [X, O, X],
        [X, O, O],
        [O, X, X]
    ]
    assert winner(board) is None

def test_terminal_win():
    board = [
        [X, X, X],
        [O, O, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    assert terminal(board) is True

def test_terminal_draw():
    board = [
        [X, O, X],
        [X, O, O],
        [O, X, X]
    ]
    assert terminal(board) is True

def test_terminal_not_over():
    board = [
        [X, O, EMPTY],
        [EMPTY, X, EMPTY],
        [O, EMPTY, EMPTY]
    ]
    assert terminal(board) is False
