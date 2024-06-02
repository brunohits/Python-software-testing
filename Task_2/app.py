import json
import logging

from flask import Flask, request, abort

from Task_1.solution import Solution

app = Flask(__name__)


@app.route("/")
def show_page():
    return "<html>" \
           "<head>" \
           "<title>App</title>" \
           "</head>" \
           "<body>" \
           "<form action='/result' method='POST'<label for='data'>Surrounded Regions</pre> (Матрица строчек)" \
           "</label><br/>" \
           "<textarea name='data' autofocus='True'></textarea>" \
           "<br/>" \
           "<input type='submit'/>" \
           "</form></body></html>"


@app.route("/result", methods=["POST"])
def show_result():
    data = request.get_json()
    if data is None:
        abort(400)
    sut = Solution()
    try:
        result = sut.solve(data)
    except ValueError:
        abort(400)
    return result, 200, {'Content-Type': 'text/plain; charset=utf-8'}


app.run()