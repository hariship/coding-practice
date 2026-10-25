import sys
from pathlib import Path

# Flask is a framework | Fast API is a framework | Django is a framework

# Types of request
# GET - get data from the server - typically used to retrieve information.
#       There won't be a data change on the server.
#       Example: client asks for the value of a. Server says 5.
# POST - send data to the server - typically for creating or updating resources.
#        Example: client sends a + 10. Server says 15.
# PUT - update data on the server - typically for saving the data on the server.
#       Example: client sends a = 20. Server saves 20.
# DELETE - delete data from the server - typically for deleting a resource.
#          Example: client asks to delete a. Server deletes a.

from flask import Flask, jsonify, request

app = Flask(__name__)

# Shared in-memory state for this example.
MEMORY = 10
# constants are usually in caps
PORT = 8000


@app.get("/value")
def get_value():
    return jsonify({"value": MEMORY})  # Jsonify returns a JSON response.


@app.post("/add")
def add_value():
    global MEMORY
    number = int(request.form["number"])
    MEMORY = MEMORY + number
    return jsonify({"message": "added", "value": MEMORY})


@app.put("/update")
def update_value():
    global MEMORY
    value = int(request.form["value"])
    MEMORY = value
    return jsonify({"message": "updated", "value": MEMORY})


@app.delete("/delete")
def delete_value():
    global MEMORY
    MEMORY = None
    return jsonify({"message": "deleted", "value": MEMORY})


if __name__ == "__main__":
    app.run(host="localhost", port=PORT)  # Turns on the server and listen in the port defined



# Job error - Failed (status code 500)
