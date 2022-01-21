from app import app, data_manager
from flask import request


@app.route('/append', methods=['PUT'])
def append():
    return data_manager.append(request)


@app.route('/show', methods=['GET'])
def show():
    return data_manager.show()
