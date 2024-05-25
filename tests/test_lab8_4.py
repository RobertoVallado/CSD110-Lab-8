from src.lab8_4 import *

def test_calculates_average1():
    data = [
        ['', '', '', '', '', '1', '', '' ],
        ['', '', '', '', '', '1', '', '' ],
        ['', '', '', '', '', '1', '', '' ],
        ['', '', '', '', '', '1', '', '' ],
        ['', '', '', '', '', '1', '', '' ],
        ['', '', '', '', '', '1', '', '' ]
    ]
    assert 1 == average_age(data), "When given data where all ages are 1, the average should be 1"

def test_calculates_average2():
    data = [
        ['', '', '', '', '', '10', '', '' ],
        ['', '', '', '', '', '20', '', '' ],
        ['', '', '', '', '', '30', '', '' ],
        ['', '', '', '', '', '40', '', '' ],
        ['', '', '', '', '', '50', '', '' ],
        ['', '', '', '', '', '60', '', '' ]
    ]
    assert 35 == average_age(data), "When given data with varying ages, your solution does not produce the expected average of 35"

def test_first_names_returns_string():
    data = [['', 'Ali', '', '', '', '', '', '' ]]
    assert str == type(first_names(data)), "The first_names function must produce a string"

def test_first_names_returns_comma_separated():
    data = [
        ['', 'Ali', '', '', '', '', '', '' ],
        ['', 'Billie', '', '', '', '', '', '' ]
    ]
    assert "Ali,Billie" == first_names(data), "The first_names function must produce a comma-separated list of names"

def test_first_names_returns_comma_separated():
    data = [
        ['', 'Billie', '', '', '', '', '', '' ],
        ['', 'Ali', '', '', '', '', '', '' ],        
    ]
    assert "Ali,Billie" == first_names(data), "The first_names function must sort the names alphabetically"