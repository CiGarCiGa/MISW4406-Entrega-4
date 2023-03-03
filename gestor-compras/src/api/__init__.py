import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))


def comenzar_consumidor(app):
    """
    Este es un código de ejemplo. Aunque esto sea funcional puede ser un poco peligroso tener 
    threads corriendo por si solos. Mi sugerencia es en estos casos usar un verdadero manejador
    de procesos y threads como Celery.
    """

    #import threading
    #import aeroalpes.modulos.cliente.infraestructura.consumidores as cliente

    # Suscripción a eventos
    #threading.Thread(target=cliente.suscribirse_a_eventos).start()

def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

     # Importa Blueprints
    from . import compra

    # Registro de Blueprints
    app.register_blueprint(compra.bp)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
