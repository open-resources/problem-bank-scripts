from problem_bank_scripts import __version__
from src.problem_bank_scripts import problem_bank_scripts as pbs
import pandas as pd

def test_version():
    assert __version__ == '0.0.11'

# def test_rounded():

#     value = 100 / 3

#     rounded_value = pbs.rounded(value, digits_after_decimal = 3)

#     assert rounded_value == str(33.333)

