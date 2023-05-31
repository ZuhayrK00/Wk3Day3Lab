from flask import render_template
from app import app
from models.order_list import *

@app.route('/')
def index():
    return render_template('index.html', title="Sean & Sons")

@app.route('/orders')
def show_orders():
    return render_template('index.html', order_list = orders)

@app.route('/orders/<num>')
def show_one(num):
    return render_template('order.html', order = orders[int(num)] )




