from homework04.task03 import my_precious_logger


def test_stdout(capsys):
    """Testing that function writes string to stdout when it doesn't start with 'error'"""
    my_precious_logger("ok")
    captured = capsys.readouterr()
    assert captured.out == "ok"


def test_stderr(capsys):
    """Testing that function writes string to stderr when it starts with 'error'"""
    my_precious_logger("error: file not found")
    captured = capsys.readouterr()
    assert captured.err == "error: file not found"
