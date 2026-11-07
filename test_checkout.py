"""Small public contract examples, not the independent holdout benchmark."""

import unittest

from checkout import total_cents


class CheckoutContractTests(unittest.TestCase):
    def test_half_up_once_after_summing(self) -> None:
        self.assertEqual(total_cents([15, 15, 15], 10), 41)
        self.assertEqual(total_cents([1, 1, 1], 50), 2)

    def test_empty_cart(self) -> None:
        self.assertEqual(total_cents([], 10), 0)

    def test_zero_and_full_discount(self) -> None:
        self.assertEqual(total_cents([15, 15, 15], 0), 45)
        self.assertEqual(total_cents([15, 15, 15], 100), 0)

    def test_exact_integer_total(self) -> None:
        self.assertEqual(total_cents([100, 200], 10), 270)

    def test_boundary_rounding(self) -> None:
        self.assertEqual(total_cents([1], 50), 1)
        self.assertEqual(total_cents([1], 51), 0)


if __name__ == "__main__":
    unittest.main()
