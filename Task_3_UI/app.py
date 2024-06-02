import json

from flask import Flask, request, abort

from Task_1_Unit.solution import Solution

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
           "<textarea name='data' autofocus='True' id='input'></textarea>" \
           "<br/>" \
           "<input type='submit' id='submit'/>" \
           "</form></body></html>"


@app.route("/result", methods=["POST"])
def show_result():
    try:
        raw_data = request.form["data"]
        data = json.loads(raw_data)
    except json.JSONDecodeError:
        abort(400)

    sut = Solution()
    try:
        result = sut.solve(data)
    except ValueError:
        abort(400)
    res = f"<html>" \
          f"<head>" \
          f"<title>App</title>" \
          f"</head>" \
          f"<body>" \
          f"<form action='/result' method='POST'<label for='data'>Surrounded Regions</pre> (Матрица строчек)" \
          f"</label><br/>" \
          f"<textarea name='data' autofocus='True' id='input'></textarea>" \
          f"<br/>" \
          f"<input type='submit' id='submit'/>" \
          f"<div id='result'>{result}</div>" \
          f"</form></body></html>"
    return res, 200, {'Content-Type': 'text/html; charset=utf-8'}


app.run()
