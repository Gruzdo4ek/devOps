from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate_sum', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    if 'values' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    values = data['values']
    try:
        total_sum = sum(float(val) for val in values)
        return jsonify({'total_sum': total_sum})
    except ValueError:
        return jsonify({'error': 'Invalid input data'}), 400

@app.route('/', methods=['GET'])
def helloworld():
    return "Hello from Flask!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)