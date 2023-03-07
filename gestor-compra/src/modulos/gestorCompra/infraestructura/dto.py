"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos

"""

from src.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Compra(db.Model):
    __tablename__ = "compra"
    id = db.Column(db.String(40), primary_key=True)
    id_orden = db.Column(db.String(40), primary_key=False, nullable=True)
    id_pago = db.Column(db.String(40), primary_key=False, nullable=True)
    id_reserva_productos = db.Column(db.String(40), nullable=True)
    productos_cantidades=db.Column(db.String(255), nullable=True)
    fecha_creacion = db.Column(db.DateTime, nullable=True)
    fecha_actualizacion = db.Column(db.DateTime, nullable=True)

class EventosCompra(db.Model):
    __tablename__ = "eventos_compra"
    id = db.Column(db.String(40), primary_key=True)
    id_entidad = db.Column(db.String(40), nullable=False)
    fecha_evento = db.Column(db.DateTime, nullable=False)
    version = db.Column(db.String(10), nullable=False)
    tipo_evento = db.Column(db.String(100), nullable=False)
    formato_contenido = db.Column(db.String(10), nullable=False)
    nombre_servicio = db.Column(db.String(40), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
