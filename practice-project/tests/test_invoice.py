from decimal import Decimal

import pytest

from invoice import invoice_total, line_total


def test_small_order_has_no_discount():
    assert line_total('2.50', 4) == Decimal('10.00')


def test_bulk_discount_starts_at_ten_items():
    assert line_total('1.00', 10) == Decimal('9.00')


def test_large_order_is_discounted():
    assert line_total('3.00', 20) == Decimal('54.00')


def test_negative_quantity_is_rejected():
    with pytest.raises(ValueError):
        line_total('1.00', -1)


def test_tax_is_added_to_the_discounted_subtotal():
    assert invoice_total([('2.50', 4), ('3.00', 20)], tax_rate='0.05') == Decimal('67.20')
