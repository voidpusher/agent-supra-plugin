"""A tiny invoice calculator used to try Agent Supra with a real failing test."""
from decimal import ROUND_HALF_UP, Decimal

BULK_QUANTITY = 10
BULK_DISCOUNT = Decimal('0.10')
CENT = Decimal('0.01')


def line_total(unit_price: str, quantity: int) -> Decimal:
    """Price for one line; orders of BULK_QUANTITY or more get the bulk discount."""
    if quantity < 0:
        raise ValueError('quantity cannot be negative')
    total = Decimal(unit_price) * quantity
    if quantity > BULK_QUANTITY:
        total -= total * BULK_DISCOUNT
    return total.quantize(CENT, rounding=ROUND_HALF_UP)


def invoice_total(lines: list[tuple[str, int]], tax_rate: str = '0') -> Decimal:
    """Sum the lines, then add tax on the discounted subtotal."""
    subtotal = sum((line_total(price, quantity) for price, quantity in lines), Decimal('0'))
    tax = (subtotal * Decimal(tax_rate)).quantize(CENT, rounding=ROUND_HALF_UP)
    return subtotal + tax
