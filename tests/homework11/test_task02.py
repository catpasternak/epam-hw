import pytest

from homework11.task02 import DiscountStrategy, Order


@pytest.fixture
def morning_discount():
    """Creates morning discount strategy class."""

    class MorningDiscount(DiscountStrategy):
        """Applies morning discout algorithm to price."""

        def count_discount(self):
            return self.price * 0.25

    return MorningDiscount


@pytest.fixture
def elder_discount():
    """Creates elder discount strategy class."""

    class ElderDiscount(DiscountStrategy):
        """Applies morning discout algorithm to price."""

        def count_discount(self):
            return self.price * 0.9

    return ElderDiscount


def test_mornign_discount_strategy_applied(morning_discount):
    """Tests that passed discount strategy is applied to price."""
    order = Order(100.00, morning_discount)
    assert order.final_price() == 75.00


def test_elder_discount_strategy_applied(elder_discount):
    """Tests that passed discount strategy is applied to price."""
    order = Order(100.00, elder_discount)
    assert order.final_price() == 10.00
