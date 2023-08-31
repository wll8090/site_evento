from flask import Flask
from rotas import rotas

def create_app():
    app=Flask(__name__)
    rotas(app)

    return app

if __name__ == '__main__':
    app=create_app()
    app.run(debug=1)