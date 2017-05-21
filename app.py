# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort

from webcrawlers import AutoEsporteWC


app = Flask(__name__)


JSON_RESPONSE_HEADERS = {'Content-Type': 'application/json'}


@app.route('/', methods=['GET'])
def index():
    return 'It works! (health check)', 200


@app.route('/feed/autoesporte/', methods=['GET'])
def autoesporte():
    autoespoete_wc = AutoEsporteWC()

    response = autoespoete_wc.get_json_content()
    if response:
        return jsonify(response), 200, JSON_RESPONSE_HEADERS

    abort(404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)
