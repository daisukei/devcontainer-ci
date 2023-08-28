import pytest

from src.main import greet, agecheck

def test_greet():
    assert greet("Alice") == "Hello, Alice!"

def test_agecheck():
    assert agecheck(17) == "You are underage."
    assert agecheck(18) == "You just became an adult."
    assert agecheck(19) == "You are an adult."

def test_agecheck_fail():
    assert agecheck(17) == "This is mistake."
