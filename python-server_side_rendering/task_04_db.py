#!/usr/bin/python3

from flask import Flask, render_template, request
from json import load
import csv
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json') as f:
        items = load(f).get('items', [])
    return render_template('items.html', items=items)


def read_json_file(file_path):
    try:
        with open(file_path) as f:
            return load(f)
    except FileNotFoundError:
        return []


def read_csv_file(file_path):
    try:
        with open(file_path) as csvFile:
            return [row for row in csv.DictReader(csvFile)]
    except FileNotFoundError:
        return []


@app.route('/products')
def products():
    source = request.args.get('source')

    if source == 'json':
        items = read_json_file('products.json')
    elif source == 'csv':
        items = read_csv_file('products.csv')
    elif source == 'sql':
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        items = [dict(row) for row in cursor.fetchall()]
        conn.close()    
    else:
        return render_template('product_display.html',
                               error='Wrong source')

    if request.args.get('id'):
        filtered_items = [item for item in items if str(
            item.get('id', '')) == request.args.get('id')]
        if not filtered_items:
            return render_template(
                'product_display.html', error='Product not found')
        items = filtered_items

    return render_template('product_display.html', items=items)


if __name__ == '__main__':
    app.run(debug=True, port=5000)