import json

from flask import Flask, Response, request
from utils import get_last_price,get_page,get_list_elements

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h2>Hola Ecuador!</h2>"
@app.route("/page")
def page():
    pagina = get_page()
    return pagina

@app.route("/api/stock")
def get_stock_price():
    company_ticker = request.args.get("ticker")

    try:
        last_price = get_last_price(ticker=company_ticker)
    except ValueError as error:
        return {"company_ticker": company_ticker, "price": None, 'error': str(error)}

    response_raw = {"company_ticker": company_ticker, "price": last_price}
    print("response_raw: ",response_raw)

    return Response(json.dumps(response_raw), mimetype='application/json')

@app.route("/api/elements")
def get_elements():
    company_ticker = request.args.get("ticker")
    try:
        values = get_list_elements(ticker=company_ticker)
    except ValueError as error:
        return {"company_ticker": company_ticker, "Valores": None, 'error': str(error)}

    response_raw = {"CompanySymbol": values[1], "Currency": values[0], "TimeZone": values[2], "PreviousPrice": values[3], "ActualPrice": values[4]}
    print("response_raw: ", response_raw)

    return Response(json.dumps(response_raw), mimetype='application/json')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)