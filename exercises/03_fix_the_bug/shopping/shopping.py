import sys
from pathlib import Path
from flask import Flask, jsonify, request

app = Flask(__name__)
Item = {"name": "item"}

port = 8001

def get_items():
    return jsonify({"items": [Item]})

def add_item(item_name):
    global Item
    Item["name"] = item_name
    return jsonify({"message": "added", "item": Item})

def has_item(item_name):
    return Item["name"] == item_name

@app.route("/has-item/<item_name>", methods=["GET"])
def check_item(item_name):
    return jsonify({"name": item_name, "exists": has_item(item_name)})