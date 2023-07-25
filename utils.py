import requests


def get_last_price(ticker: str) -> float:
    """
    Esta funcion busca usando la API de yahoo finance el ultimo precio disponible del instrumento cuyo ticker es 'ticker'.
    @:param ticker: ticker de la empresa a consultar
    """
    yahoo_finance_url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    # yahoo_finance_url = "https://query1.finance.yahoo.com/v8/finance/chart/" + ticker  # lo mismo que arriba
    headers = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url=yahoo_finance_url, headers=headers)
    if r.json().get('chart') is None:
        raise ValueError(f"ticker: '{ticker}' not found")

    price = r.json().get('chart').get('result')[0].get('meta').get('regularMarketPrice')

    print(r.json())
    return price


def get_list_elements(ticker: str):
    """
    Esta funcion busca usando la API de yahoo finance varios elementos en función de  cuyo ticker es 'ticker'.
    @:param ticker: ticker de la empresa a consultar
    """
    elements = []
    yahoo_finance_url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    # yahoo_finance_url = "https://query1.finance.yahoo.com/v8/finance/chart/" + ticker  # lo mismo que arriba
    headers = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url=yahoo_finance_url, headers=headers)
    if r.json().get('chart') is None:
        raise ValueError(f"ticker: '{ticker}' not found")
    print(r.json())
    cu = r.json().get('chart').get('result')[0].get('meta').get('currency')
    sy = r.json().get('chart').get('result')[0].get('meta').get('symbol')
    ex = r.json().get('chart').get('result')[0].get('meta').get('exchangeTimezoneName')
    pc = r.json().get('chart').get('result')[0].get('meta').get('previousClose')
    pa = r.json().get('chart').get('result')[0].get('meta').get('regularMarketPrice')

    for i in (cu,sy,ex,pc,pa):
      elements.append(i)

    return elements

def get_page():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tratamiento de Datos - Página de Inicio</title>
        <style>
           
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #EAAA00;
                
            }
            header {
                background-color: #333;
                color: #fff;
                text-align: center;
                padding: 1rem;
            }
            .container {
                max-width: 990px;
                margin: 0 auto;
                padding: 2rem;
                color: #002d72;
            }
            h1 {
                color: #2d7200;
            }
            p {
                line-height: 1.6;
                color: #555;
            }
            footer {
                background-color: #333;
                color: #fff;
                text-align: center;
                padding: 1rem;
                position: absolute;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Tratamiento de Datos con Iván</h1>
        </header>
        <div class="container">
            <h2>Bienvenido a nuestra página de inicio</h2>
            <p>En nuestro sitio web, encontrarás información y recursos relacionados con el tratamiento de datos.
             Nos dedicamos a explorar las mejores prácticas para la recopilación, procesamiento, almacenamiento y análisis de datos.</p>
            <p>Algunos temas que cubrimos incluyen:</p>
            <ul>
                <li>Generación de Apis</li>
                <li>Consulta de Apis</li>
                <li>Visualización de datos</li>

            </ul>
            <p>¡Explora nuestros artículos y recursos para obtener más información sobre este emocionante campo!</p>
        </div>
        <footer>
            <p>Derechos Reservados &copy; 2023 | Tratamiento de Datos</p>
        </footer>
    </body>
    </html> """
