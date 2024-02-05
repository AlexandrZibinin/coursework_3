import pytest

from coursework_3.func import *


def test_five_operations():
    assert five_operations([0, 1, 2, 3, 4, 5, 6]) == [0, 1, 2, 3, 4]
    assert five_operations([0, 1, 2, 3, 4, 5, 6]) != [0, 1, 2, 3, 4, 5]


def test_get_dict_from_json():
    with pytest.raises(FileNotFoundError):
        get_dict_from_json('operation.json')


def test_get_executed():
    assert get_executed([]) == []
    assert get_executed(['EXECUTED']) == []
