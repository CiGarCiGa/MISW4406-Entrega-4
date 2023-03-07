# Entregas de los Alpes

## Propuesta
Se implementa una prueba de concepto a la siguiente arquitectura de solución inicialmente propuesta

![Componentes-v2](https://user-images.githubusercontent.com/9620295/223312301-e42da9ac-129e-4d5d-a9ab-749a6eed2911.png)

la cual estará enfocada en los siguientes microservicios:
* GestorCompra
* AdministrarProductos
* ConsolidadorProductos

Para efectos de la prueba de concepto, se propone la siguiente arquitectura para la experimentación:

![Componentes-Page-4](https://user-images.githubusercontent.com/9620295/223312278-0ae12cff-1ebc-42ae-8f7b-46d6bdd8264a.png)

De acuerdo al diagrama anterior, se propone validar a través de escenarios de calidad los siguientes flujos:
* Una vez llega una solicitud de orden de compra al servicio GestorCompra, se debe realizar la validación de los productos de la orden en inventario. Si algun(os) productos no esta(n) en inventario, se debe notificar de vuelta. Así mismo, si todos los productos están en inventario, se debe notificar.
* Una vez llega una solicitud de orden de compra y se validan los productos en inventario, se deben reservar los productos de la orden para poder generar la orden de compra.

## Escenarios de calidad
Se proponen los siguientes escenarios de calidad para validar la prueba de concepto, tomando en cuenta los flujos anteriores:

...
...
...

## GestorCompra
Tiene dos responsabilidades:
* Enviar a *Consolidador* los productos de la orden para validar si están en inventario, a través del envío del comando *ValidarInventario*. Luego, recibe la respuesta de la validación consumiendo el evento *InventarioValidado*.
* ...


## AdministrarProductos
...

## ConsolidadorProductos
Se implementa el microservicio *Consolidador* que, para efectos de la prueba de concepto, valida si los productos de la orden se encuentran en inventario. Funciona de la siguiente manera:
* Consume el comando *ValidarInventario* enviado por *GestorCompra* para conocer los productos de la orden a validar
* Responde el resultado de la validación enviando el evento *InventarioValidado* a GestorCompra

## Decisiones tomadas
* Se implementan los microservicios utilizando flask/python
* Se utiliza Avro para la serialización de datos 
* Para el almacenamiento de datos, se propone una administración de los mismos híbrida, ya que los servicios *AdministrarProductos* y *ConsolidadorProductos* comparten una base de datos, mientras que *Gestorcompra* y *Ordenes* tienen cada uno su respectiva base de datos
