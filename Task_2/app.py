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
            "<body>"\
                "<form action='/result' method='POST'<label for='data'>Input strings', '</pre>(coc)"\
        "</label><br/>"\
        "<textarea name='data' autofocus='True'></textarea>"\
        "<br/>"\
        "<input type='submit'/>"\
        "</form></body></html>"
@app.route("/result", methods=["POST"])
def show_result():
    logging.error(request.form.keys(), request.form['data'])
    if list(request.form.keys())!=['data']:
        abort(400)
    sut = Solution()
    data = request.form['data']
    data = json.loads(data)
    try:
        result = sut.solve(data)
    except ValueError:
        abort(400)
    return result, 200, {'Content-Type': 'text/plain; charset=utf-8'}

app.run()