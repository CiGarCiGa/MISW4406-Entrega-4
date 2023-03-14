import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    import src.modulos.orden.aplicacion


def comenzar_consumidor(app):
    import threading
    import src.modulos.orden.infraestructura.consumidores as cliente
    # Suscripción a eventos
    threading.Thread(target=cliente.suscribirse_a_comandos, args=[app]).start()
    threading.Thread(target=cliente.consumidor_inicio_flujo, args=[app]).start()

def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

     # Importa Blueprints
    from . import orden

    # Registro de Blueprints
    app.register_blueprint(orden.bp)

    registrar_handlers()
    comenzar_consumidor(app)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
