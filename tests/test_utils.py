import pytest
from utils import mask_from, mask_to, change_format_data




def test_mask_from():
    assert mask_from("Visa Gold 5999414228426353") == "Visa Gold 5999 41** **** 6353"
    assert mask_from("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_mask_to():
    assert mask_to("Счет 72731966109147704472") == "Счет **4472"

def test_change_format_data():
    assert change_format_data("2018-04-04T17:33:34.701093") == "04.04.2018"