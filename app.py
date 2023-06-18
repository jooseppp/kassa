from dataclasses import dataclass

from flask import Flask, request

from writer import create_transactions,add_to_customer

app = Flask(__name__)


@dataclass
class Order:
    customer_name: str
    drink_name: str
    quantity: int


@app.route('/order', methods=['POST'])
def order():
    try:
        data = Order(request.json['customer_name'], request.json['drink_name'], request.json['quantity'])
        add_to_customer(data.customer_name, data.drink_name, data.quantity)

        return "ok"
    except Exception as e:
        print(e)
        return e


if __name__ == '__main__':
    app.run(debug=True)
