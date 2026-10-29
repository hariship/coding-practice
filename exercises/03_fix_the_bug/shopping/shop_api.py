import sys
from pathlib import Path
from flask import Flask, jsonify, request
import shopping


app = Flask(__name__)

port = 8001

@app.get("/items")
def get_items():
    return jsonify({"items": shopping.get_items()})

@app.get("/items/count")
def count_items():
    return jsonify({"count": shopping.count()})


@app.post("/items")
def add_item():
    item = request.form.get("item", "").strip()

    if not item:
        return jsonify({
            "error": "item can't be empty"
        }), 400

    return jsonify({
        "message": "added",
        "items": shopping.add_item(item)
    })


@app.put("/items")
def replace_item():
    old = request.form.get("old", "").strip()
    new = request.form.get("new", "").strip()

    if not old or not new:
        return jsonify({
            "error": "item can't be empty"
        }), 400

    if not shopping.has_item(old):
        return jsonify({
            "error": f"{old} is not in the list"
        }), 404

    return jsonify({
        "message": "replaced",
        "items": shopping.replace_item(old, new)
    })


@app.delete("/items")
def delete_item():
    item = request.form.get("item", "").strip()

    if not item:
        return jsonify({
            "error": "item can't be empty"
        }), 400

    if not shopping.has_item(item):
        return jsonify({
            "error": f"{item} is not in the list"
        }), 404

    return jsonify({
        "message": "removed",
        "items": shopping.remove_item(item)
    })


if __name__ == "__main__":
    app.run(host="localhost", port=PORT)  # Turns on the server and listen in the port defined
    
