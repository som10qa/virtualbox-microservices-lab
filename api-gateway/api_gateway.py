from flask import Flask, jsonify
import requests

app = Flask(__name__)

USER_SERVICE = "http://192.168.56.101:5001/users"
PRODUCT_SERVICE = "http://192.168.56.102:5002/products"
ORDER_SERVICE = "http://192.168.56.103:5003/orders"

@app.route('/users')
def users():
    return requests.get(USER_SERVICE).json()

@app.route('/products')
def products():
    return requests.get(PRODUCT_SERVICE).json()

@app.route('/orders')
def orders():
    return requests.get(ORDER_SERVICE).json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
