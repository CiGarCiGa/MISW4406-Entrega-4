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

### Escalabilidad
<img width="950" alt="Screen Shot 2023-03-07 at 4 30 20 PM" src="https://user-images.githubusercontent.com/9620295/223557352-ba5b2616-cca5-4256-a932-f6403eb0ebb4.png">

### Desempeño
<img width="950" alt="Screen Shot 2023-03-07 at 4 34 28 PM" src="https://user-images.githubusercontent.com/9620295/223558147-4f819080-8e76-4811-9759-d3af551a61e8.png">

### Disponibilidad
<img width="950" alt="Screen Shot 2023-03-07 at 4 22 44 PM" src="https://user-images.githubusercontent.com/9620295/223556099-31db5ab8-e13e-46e4-a4f3-e530634504bf.png">

## GestorCompra
Tiene las siguientes responsabilidades:
* Funciona como orquestador y se comunica con los diferentes servicios para completar la transacción de la compra. En caso de fallo, es necesario realizar la compensanción sobre cada uno de los servicos, publicando el comando de rollback en cada topico.
* Envia a *Consolidador* los productos de la orden para validar si están en inventario, a través del envío del comando *ValidarInventario*. Luego, recibe la respuesta de la validación consumiendo el evento *InventarioValidado*.
* Envia a *admin-prodcutos* los productos de la orden que debe reserva, a través del envío del comando *ReservarProducto*. Luego recibe la respuesta de la reserva consumiendo el evento *ProductosReservados*
* Envía a *ordenes* la solicitud de creación de una orden. Luego recibe la respuesta de la creación de la orden consumiendo el evento "OrdenCreada". 
Con estos tres procesos la transación se completa.

## AdministrarProductos
Se implementa el microservicio *admin-productos* que para la efectos de la prueba de concepto, manipula la información del stock de inventario. En este caso particular, toma la información de los productos, y los inserta en una tabla "Reserva". Los productos contenido en esta tabla quedaran alli hasta que sean despachados. Adicionalmente se descuenta de la cantidad de productos en el inventario ofrecidos al público. En caso de fallo de la compra, por alguna razón, es posible revertir la operación liberando los productos y agregando dichos productos nuevamente al inventario (tabla "Producto").

## ConsolidadorProductos
Se implementa el microservicio *Consolidador* que, para efectos de la prueba de concepto, valida si los productos de la orden se encuentran en inventario. Funciona de la siguiente manera:
* Consume el comando *ValidarInventario* enviado por *GestorCompra* para conocer los productos de la orden a validar
* Responde el resultado de la validación enviando el evento *InventarioValidado* a GestorCompra

## Decisiones tomadas
* Se implementan los microservicios utilizando flask/python
* Se utiliza Avro para la serialización de datos 
* Para el almacenamiento de datos, se propone una administración de los mismos híbrida, ya que los servicios *AdministrarProductos* y *ConsolidadorProductos* comparten una base de datos, mientras que *Gestorcompra* y *Ordenes* tienen cada uno su respectiva base de datos.

## Instruccion para iniciar la aplicación
Utilizar docker-compose para levantar el sistema de la siguiente manera
1. Descargar el repositorio
2. Hacer uso de los comandos docker-compose para levantar pulsar
> docker-compose --profile pulsar up
3. Hacer uso de los comandos docker-compose para levantar las bases de datos
> docker-compose --profile db up
4. Hacer uso de los comandos los servicios faltantes
> docker-compose --profile consolidador --profile admin-productos --profile gestor-compra up

##Distribución de trabajo:
- Marisela: creacion de consolidador
- Carlos: creacion de Gestor compra, admin-productos
- Oscar: genración de SAGA
- Juan: realizar BBF
