from typing import NoReturn, Optional

import pytest

from homework.hw4.task3_get_print_output import my_precious_logger


@pytest.mark.parametrize(
    ("for_stderr_input", "for_stdout_input"),
    [
        ("error, someone help", "this time fine"),
    ],
)
def test_logger_outputs(
    capsys, for_stderr_input, for_stdout_input
) -> Optional[NoReturn]:
    my_precious_logger(for_stderr_input)
    my_precious_logger(for_stdout_input)
    captured = capsys.readouterr()
    assert captured.out == for_stdout_input
    assert captured.err == for_stderr_input
