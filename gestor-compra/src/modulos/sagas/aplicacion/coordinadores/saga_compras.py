from seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from seedwork.aplicacion.comandos import Comando
from seedwork.dominio.eventos import EventoDominio

from src.modulos.sagas.dominio.eventos.gestorcompra import CompraCreada, CreacionCompraFallida
from src.modulos.sagas.dominio.eventos.consolidador import InventarioValidado, ValidacionInventarioFallida
from src.modulos.sagas.aplicacion.comandos.crear_compra import CrearCompra
from src.modulos.sagas.aplicacion.comandos.cancelar_compra import CancelarCompra


class CoordinadorCompras(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearCompra, evento=CompraCreada, error=CreacionCompraFallida, compensacion=CancelarCompra),
            Transaccion(index=2, comando=ValidarInventario, evento=InventarioValidado, error=ValidacionInventarioFallida, compensacion=CancelarValidacionInventario),
            Transaccion(index=3, comando=ReservarProducto, evento=ProductoReservado, error=ReservaProductoFallida, compensacion=CancelarReservaProducto),
            Transaccion(index=4, comando=CrearOrden, evento=OrdenCreada, error=CreacionOrdenFallida, compensacion=CancelarCreacionOrden),
            Fin(index=5)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])

    def terminar():
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorCompras()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
