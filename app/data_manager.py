import os

from flask import request, jsonify
from app import app


STORED_STR: set = set()


def append(req: request):
    """
    This function is to call directly from the route, it checks the request content.

    :param req: request parameter
    :type req: request
    :return:
    """
    try:
        item = req.json['item']
    except KeyError:
        return jsonify(message='No item found to append.'), 400
    except TypeError:
        return jsonify(message='Invalid data'), 400
    return store_str(item=item)


def store_str(item: str):
    """
    This function calls the storing function based on the currently set storage type.

    :param item: the string item to be stored
    :type item: str
    :return:
    """
    storage_methods: dict = {
        'store_in_memory': 'store_in_memory',
        'store_on_filesystem': 'store_on_filesystem'
    }
    storage_method = storage_methods.get(app.config['_STORAGE_TYPE'], 'config_error')
    return eval(f'{storage_method}(item)')


def store_in_memory(item: str):
    """
    This function will append the received value to the STORED_STR set.
    :param item:
    :return:
    """
    STORED_STR.add(item)
    return jsonify(message='Success'), 200


def store_on_filesystem(item: str):
    """
    This function will append the received value to a file.

    :param item:
    :return:
    """
    content_set: set = set()
    try:
        with open(app.config['_FILE_NAME'], 'r+') as file:
            content_set: set = set(file.read().split(','))
    except IOError:
        pass
    try:
        with open(os.path.join(os.getcwd(), app.config['_FILE_NAME']), 'w+') as file:
            content_set.add(item)
            file.write(','.join(content_set))
    except IOError as e:
        return jsonify(message=f'Error while appending to file, details: {e}'), 500
    return jsonify(message='Success'), 200


def config_error(*args):
    """
    This function is to be called when the application has not been configured properly.

    :param args:
    :return:
    """
    return jsonify(message='Invalid configuration'), 400


def show():
    """
    This function calls the return function based on the currently set storage type.

    :return:
    """
    storage_methods: dict = {
        'store_in_memory': 'show_from_memory',
        'store_on_filesystem': 'show_from_filesystem'
    }
    storage_method = storage_methods.get(app.config['_STORAGE_TYPE'], 'config_error')
    return eval(f'{storage_method}()')


def show_from_filesystem():
    """
    This function will return the content of the stored file.

    :return:
    """
    try:
        with open(app.config['_FILE_NAME'], 'r') as file:
            content = file.read()
    except IOError as e:
        return jsonify(message=f'Error while reading file, details: {e}'), 500
    return jsonify(message=content), 200


def show_from_memory():
    """
    This function will return all the values stored the STORED_STR set.

    :return:
    """
    return jsonify(message=','.join(STORED_STR)), 200
