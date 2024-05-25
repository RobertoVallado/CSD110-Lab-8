
from src.lab8_3 import csv2list

def test_column_file():
    assert [['1'], ['2'], ['3']] == csv2list("tests/data_8_3_1.csv"), """csv2list did not produce the correct list when loading data_8_3_1.csv"""

def test_row_file():
    assert [['1', '2', '3']] == csv2list("tests/data_8_3_2.csv"), """csv2list did not produce the correct list when loading data_8_3_2.csv"""

def test_2d_file():
    expected = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    assert expected == csv2list("tests/data_8_3_3.csv"), """csv2list did not produce the correct list when loading data_8_3_3.csv"""