import pytest

from homework.hw7.task3_tac_tic_help import tic_tac_toe_checker

table_unfin = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]]

table_x = [["-", "-", "o"], ["-", "o", "o"], ["x", "x", "x"]]

table_o = [["-", "-", "o"], ["-", "o", "o"], ["o", "x", "x"]]

table_draw = [["o", "x", "o"], ["x", "x", "o"], ["o", "o", "x"]]


@pytest.mark.parametrize(
    ("table", "expected_result"),
    [
        (table_x, "x wins!"),
        (table_o, "o wins!"),
        (table_unfin, "unfinished!"),
        (table_draw, "draw!"),
    ],
)
def test_tic_tac_toe_checker(table, expected_result):
    actual_result = tic_tac_toe_checker(table)
    assert actual_result == expected_result
