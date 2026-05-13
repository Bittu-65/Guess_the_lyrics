from project import make_blank, give_hint
import pytest

def test_make_blank(): 
    line = "I knew you were trouble when you walked in"
    blanked, answer = make_blank(line)
    assert blanked is not None
    assert answer is not None
    assert "_____" in blanked
    assert answer in line

def test_make_blank_short_line():
    line = "hi"
    blanked, answer = make_blank(line)
    assert blanked is None
    assert answer is None

def test_give_hint_first():
    hint = give_hint("trouble", 0)
    assert "t" in hint.lower()

def test_give_hint_length():
    hint = give_hint("trouble", 1)
    assert "7" in hint

def test_give_hint_first_last():
    hint = give_hint("trouble", 2)
    assert "t" in hint.lower()
    assert "e" in hint.lower()

def test_give_hint_no_more():
    hint = give_hint("trouble", 3)
    assert "No more" in hint