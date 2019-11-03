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
    assert str(c) == "8 dl"

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

def test_convert_to_dl(two_amount_objects):
    a, b = two_amount_objects
    c = AmountLiter(0.15)
    assert str(a) == "5 dl"
    assert str(b) == "3 dl"
    assert str(c) == "1 1/2 dl"

def test_convert_to_msk():
    a = AmountLiter(0.015)
    b = AmountLiter(0.03)
    assert str(a) == "1 msk"
    assert str(b) == "2 msk"

def test_convert_to_tsk():
    a = AmountLiter(0.01)
    assert str(a) == "2 tsk"

def test_convert_to_krm():
    a = AmountLiter(0.004)
    assert str(a) == "4 krm"

def test_convert_to_half_of_piece():
    a = AmountPiece(0.5)
    b = AmountPiece(1.5)
    assert str(a) == "1/2 piece"
    assert str(b) == "1 1/2 piece"
