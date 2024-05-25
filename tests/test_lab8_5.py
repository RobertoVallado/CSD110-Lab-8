from src.lab8_5 import *

def test_map1():
    data = [
        [ '1', 'first1', 'last1', '', '', '', '', '', '' ],
        [ '2', 'first2', 'last2', '', '', '', '', '', '' ],
        [ '3', 'first3', 'last3', '', '', '', '', '', '' ]
    ]
    datacopy = data[:]
    expected = [ 'first1 last1', 'first2 last2', 'first3 last3' ]
    assert expected == map_to_fullname(data), "The map_to_fullname function does not produce the correct result"
    assert data == datacopy, "The map function must leave the original 2-d list unchanged"

def test_map2():
    data = [
        [ '1', 'a', 'b', '', '', '', '', '', '' ],
        [ '2', 'c', 'd', '', '', '', '', '', '' ],
        [ '3', 'e', 'f', '', '', '', '', '', '' ],
        [ '4', 'g', 'h', '', '', '', '', '', '' ],
        [ '5', 'i', 'j', '', '', '', '', '', '' ]
    ]
    expected = [ 'a b', 'c d', 'e f', 'g h', 'i j' ]
    assert expected == map_to_fullname(data), "The map_to_fullname function does not produce the correct result"

def test_filter1():
    data = [
        [ '1', '', '', 'Male', 'France', '', '', '', '' ],
        [ '2', '', '', 'Male', 'France', '', '', '', '' ],
        [ '3', '', '', 'Male', 'France', '', '', '', '' ]
    ]
    datacopy = data[:]
    assert data == filter_french_males(data), "If the given list has only French males, the returned list should be the same as the original"
    assert data == datacopy, "The filter function must leave the original 2-d list unchanged"

def test_filter2():
    data = [
        [ '1', '', '', 'Male', 'Britain', '', '', '', '' ],
        [ '2', '', '', 'Female', 'France', '', '', '', '' ],
        [ '3', '', '', 'Male', 'United States', '', '', '', '' ]
    ]
    assert [] == filter_french_males(data), "If the given list has no French males, the returned list should be empty"

def test_filter3():
    data = [
        [ '1', '', '', 'Male', 'Britain', '', '', '', '' ],
        [ '2', '', '', 'Male', 'France', '', '', '', '' ],
        [ '3', '', '', 'Female', 'France', '', '', '', '' ],
        [ '4', '', '', 'Male', 'France', '', '', '', '' ]
    ]
    expected = [
        [ '2', '', '', 'Male', 'France', '', '', '', '' ],
        [ '4', '', '', 'Male', 'France', '', '', '', '' ]
    ]
    actual = filter_french_males(data)
    assert expected == actual, "The returned list should contain ONLY entries containing French males"
    assert not (actual[0] is data[1]) and not (actual[1] is data[3]), "The items in the list returned from filter_french_males must be COPIES, not references"

def test_reduce1():
    data = [
        [ '1', '', '', 'Male', 'Britain', '25', '', '', '' ],
        [ '2', '', '', 'Male', 'France', '65', '', '', '' ],
        [ '3', '', '', 'Female', 'France', '87', '', '', '' ],
        [ '4', '', '', 'Male', 'France', '34', '', '', '' ]
    ]
    datacopy = data[:]
    actual = reduce_to_oldest(data)
    assert data[2] == actual, "The reduce_to_oldest function should return the row representing the oldest person"
    assert data == datacopy, "The reduce function must leave the original 2-d list unchanged"
    assert not actual is data[2], "The item returned from reduct_to_oldest must be a COPY, not a reference"

def test_reduce2():
    data = [
    ]
    assert None == reduce_to_oldest(data), "The reduce_to_oldest function should return None if the given people list is empty"

def test_reduce3():
    data = [
        [ '1', '', '', 'Male', 'Britain', '25', '', '', '' ],
    ]
    assert data[0] == reduce_to_oldest(data), "If the given people list has only one row, the reduce_to_oldest function should return that row"