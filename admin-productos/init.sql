-- productos.eventos_producto definition

CREATE TABLE `eventos_producto` (
  `id` varchar(40) NOT NULL,
  `id_entidad` varchar(40) NOT NULL,
  `fecha_evento` datetime NOT NULL,
  `version` varchar(10) NOT NULL,
  `tipo_evento` varchar(100) NOT NULL,
  `formato_contenido` varchar(10) NOT NULL,
  `nombre_servicio` varchar(40) NOT NULL,
  `contenido` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- productos.productos definition

CREATE TABLE `productos` (
  `id` varchar(40) NOT NULL,
  `nombre` varchar(40) DEFAULT NULL,
  `cantidad` int NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  `fecha_actualizacion` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- productos.productos_reservados definition

CREATE TABLE `productos_reservados` (
  `id` varchar(40) NOT NULL,
  `id_producto` varchar(40) DEFAULT NULL,
  `id_compra` varchar(40) DEFAULT NULL,
  `cantidad` int NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('1', 'Producto1', 500, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('2', 'Producto2', 400, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('3', 'Producto3', 500, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('4', 'Producto4', 300, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('5', 'Producto5', 500, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('6', 'Producto6', 300, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('7', 'Producto7', 500, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('8', 'Producto8', 400, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('9', 'Producto9', 100, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('10', 'Producto10', 500, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('11', 'Producto11', 1000, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('12', 'Producto12', 500, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('13', 'Producto13', 50, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('14', 'Producto14', 10, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('15', 'Producto15', 0, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('16', 'Producto16', 500, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('17', 'Producto17', 500, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
INSERT INTO productos.productos (id, nombre, cantidad, fecha_creacion, fecha_actualizacion) VALUES('18', 'Producto18', 500, '2023-03-04 22:25:31', '2023-03-04 22:25:38');
