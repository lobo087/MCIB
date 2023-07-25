from api import get_stock_price


def test_get_stock_price():
    cocacola_price = get_stock_price('KO').json
    print(cocacola_price)

    assert cocacola_price['price'] > 0

    assert get_stock_price('FANTAL').status_code == 404


test_get_stock_price()
