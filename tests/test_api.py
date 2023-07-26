from api import get_stock_price
from utils import get_last_price


def test_get_stock_price():
    cocacola_price = get_last_price('KO')
    print(cocacola_price)

    assert cocacola_price > 0


test_get_stock_price()
