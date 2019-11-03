import pytest
from gimme_food.entities.amount import Amount, AmountPiece, AmountLiter, AmountUnknown
from gimme_food.entities.amount import IncompatibleAmountTypes

@pytest.fixture
def amount_object():
    return AmountPiece(5)

@pytest.fixture
def two_amount_objects():
    return AmountLiter(0.5), AmountLiter(0.3)

@pytest.fixture
def unknown_amount_object():
    return AmountUnknown("unknown")

def test_print_amount(amount_object):
    amount_str = str(amount_object)
    assert amount_str == "5 piece"

def test_sum(two_amount_objects):
    a, b = two_amount_objects
    c = a.sum(b)
    assert str(c) == "0.8 liter"

def test_sum_empty_dict(amount_object):
    a = amount_object.sum({})
    assert str(a) == "5 piece"

def test_sum_with_unknown(amount_object, unknown_amount_object):
    a = amount_object
    b = unknown_amount_object
    c = a.sum(b)
    d = b.sum(a)
    assert str(c) == "5 piece"
    assert str(d) == "5 piece"

def test_incompatible_types(amount_object, two_amount_objects):
    a = amount_object
    b = two_amount_objects[0]
    with pytest.raises(IncompatibleAmountTypes):
        a.sum(b)
