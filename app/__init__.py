from flask import Flask

app = Flask(__name__)
app.config.from_object('config.Config')

from app import routes


if __name__ == '__main__':
    """
    This is the entry point of the application.
    """
    app.run(debug=True)
