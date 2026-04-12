from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

@app.route("/alkuluku/<int:number>", methods=["GET"])
def check_prime(number):
    return jsonify({
        "Number": number,
        "isPrime": is_prime(number)
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)