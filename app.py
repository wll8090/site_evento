from flask import Flask
from rotas import pages

def create_app():
    app=Flask(__name__)
    pages(app)

    return app

if __name__ == '__main__':
    app=create_app()
    app.run(debug=1)
#python!
