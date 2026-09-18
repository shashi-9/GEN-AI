from flask import Flask, jsonify

app = Flask(__name__)


# Factorial Function
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


# Armstrong Function
def is_armstrong(n):
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total = total + (digit ** digits)
        n = n // 10

    return total == original


# Factorial API
@app.route('/factorial/<int:number>', methods=['GET'])
def factorial_api(number):

    if number < 0:
        return jsonify({
            "error": "Factorial is not defined for negative numbers"
        })

    result = factorial(number)

    return jsonify({
        "number": number,
        "factorial": result
    })


# Armstrong API
@app.route('/armstrong/<int:number>', methods=['GET'])
def armstrong_api(number):

    result = is_armstrong(number)

    return jsonify({
        "number": number,
        "is_armstrong": result
    })


# Home API
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Python Flask API",
        "available_apis": [
            "/factorial/<number>",
            "/armstrong/<number>"
        ]
    })


if __name__ == '__main__':
    app.run(debug=True)