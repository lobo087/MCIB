from api import get_stock_price


def test_get_stock_price():
    cocacola_price = get_last_price('KO').json
    print(cocacola_price)

    assert cocacola_price['price'] > 0


test_get_stock_price()
