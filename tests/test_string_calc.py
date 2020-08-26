from string_calc import *
import pytest

subject = StringCalc()

def test_return_0_for_empty_string():
    assert subject.add_num("") == 0

def test_return_single_str_num_as_int():
    assert subject.add_num("1") == 1

def test_return_added_strs_as_int():
    assert subject.add_num("1,2") == 3

def test_3_args():
    assert subject.add_num("1,2,3") == 6

def test_5_args():
    assert subject.add_num("3,3,3,3,3") == 15

def test_input_seperated_by_linebreaks():
    assert subject.add_num("1\n2,3") == 6

def test_change_delimiter():
    assert subject.add_num("//;\n1;2") == 3

def test_change_delimiter_2():
    assert subject.add_num("//!\n4!2") == 6

def test_negatives_not_allowed():
    with pytest.raises(ValueError) as e:
        subject.add_num("1, -1")
    assert e.type is ValueError

def test_return_multiple_negative_numbers():
    with pytest.raises(ValueError) as e:
        subject.add_num("1, -1, -2, 3")
    assert e.type is ValueError

def test_numbers_above_1000_ignored():
    assert subject.add_num("1, 2, 1001") == 3

def test_delimiter_in_square_brakets():
    assert subject.add_num("//[***]\n1***2***3") == 6

# def test_delimiter_in_square_brakets_mismatch():
#     assert subject.add_num("//[**]\n1***2***3") == 6

def test_two_delimiters():
    assert subject.add_num("//[*][%]\n1*2%5") == 8

def test_two_delimiters_multiple():
    assert subject.add_num("//[**][??]\n1**2??5") == 8

