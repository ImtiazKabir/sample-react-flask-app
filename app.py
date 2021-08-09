from flask import Flask, request, jsonify, send_from_directory
from flask_cors import cross_origin

from math import factorial


app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
  return send_from_directory(app.static_folder, 'index.html')


@app.route('/calc', methods=['POST'])
@cross_origin()
def calc():
  req = request.get_json(force=True)
  num = int(req['n'])
  fact = factorial(num)
  response = {
    'factorial': str(fact),
    'success': True
  }
  return jsonify(response)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
