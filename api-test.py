from test import get_subarreglo
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/get-subarreglo', methods=['POST'])
def subarreglo():
    data = request.get_json()
    array = data.get('array')
    target = data.get('target')
    result = get_subarreglo(array, target)
    return jsonify({"subarray": result})

if __name__ == '__main__':
    app.run(debug=True)