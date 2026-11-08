# Correct checkout refactor: apply the discount once to the full subtotal.


def total_cents(prices_cents: list[int], discount_percent: int) -> int:
    subtotal = sum(prices_cents)
    return (subtotal * (100 - discount_percent) + 50) // 100
