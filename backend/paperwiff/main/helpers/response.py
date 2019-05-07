from flask import jsonify

def response(message):
    return jsonify({
        "result": message,
    })