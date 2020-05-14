import pytest
from src.exercise import main

def test_exercise(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == "Once upon a time\nthere was\na program\n", "Should read:\n 'Once upon a time\nthere was\na program\n'"
