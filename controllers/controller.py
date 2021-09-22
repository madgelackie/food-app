from app import app
from models.order_objects import orders
from flask import render_template


@app.route('/orders')
def index():
    return render_template("index.html", title="Home", orders=orders)

@app.route('/orders/<index>')
def order(index):
    order = orders[int(index)]
    return render_template("order.html", title='Order details', order=order)

