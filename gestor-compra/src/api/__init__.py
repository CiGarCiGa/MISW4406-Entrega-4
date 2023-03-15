import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger
#import asyncio

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))
tasks = list()

#def registrar_handlers():
#    import src.modulos.sagas.aplicacion

def importar_modelos_alchemy():
    import src.modulos.gestorCompra.infraestructura.dto

def comenzar_consumidor(app):
    import threading
    import src.modulos.gestorCompra.infraestructura.consumidores as gestor
    import src.modulos.inventario.infraestructura.consumidores as gestor_inventario
    import src.modulos.orden.infraestructura.consumidores as gestor_orden

    #import src.modulos.sagas.infraestructura.consumidores as saga
    #from src.modulos.sagas.infraestructura.schema.v1.eventos import CompraIniciada

    # Suscripción a eventos
    threading.Thread(target=gestor.suscribirse_a_comandos, args=[app]).start()
    threading.Thread(target=gestor.suscribirse_a_eventos, args=[app]).start()
    threading.Thread(target=gestor.consumidor_inicio_flujo, args=[app]).start()
    threading.Thread(target=gestor.suscribirse_a_eventos_productos, args=[app]).start()

    threading.Thread(target=gestor_inventario.suscribirse_a_eventos, args=[app]).start()
    threading.Thread(target=gestor_inventario.suscribirse_a_comandos, args=[app]).start()

    threading.Thread(target=gestor_inventario.consumidor_inicio_flujo, args=[app]).start()

    threading.Thread(target=gestor_orden.suscribirse_a_eventos, args=[app]).start()
    threading.Thread(target=gestor_orden.consumidor_inicio_flujo, args=[app]).start()

    #asyncio.ensure_future(saga.suscribirse_a_topico("eventos-bff", "bff-cliente", CompraIniciada))

def create_app(configuracion={}):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

     # Inicializa la DB
    from src.config.db import init_db, database_connection

    app.config['SQLALCHEMY_DATABASE_URI'] = database_connection(configuracion, basedir=basedir)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_db(app)

    from src.config.db import db

    importar_modelos_alchemy()
    #registrar_handlers()

     # Importa Blueprints
    from . import gestor

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor(app)

        #from src.modulos.sagas.aplicacion.coordinadores.saga_compras import CoordinadorCompras
        #CoordinadorCompras()

    # Registro de Blueprints
    #app.register_blueprint(gestor.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
