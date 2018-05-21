PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE `productos` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`codigo`	string NOT NULL UNIQUE,
	`nombre`	string NOT NULL,
	`precio`	REAL NOT NULL
);
CREATE TABLE `proveedores` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`nombre`	string NOT NULL,
	`numero_documento`	string NOT NULL
);
CREATE TABLE `sistema_pagos` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`codigo`	string NOT NULL UNIQUE,
	`nombre`	string NOT NULL
);
INSERT INTO "sistema_pagos" VALUES(1,'t.c.','Crédito');
INSERT INTO "sistema_pagos" VALUES(3,'t.d.','Débito');
INSERT INTO "sistema_pagos" VALUES(4,'cont','Contado');
CREATE TABLE `servicios` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`codigo`	string NOT NULL UNIQUE,
	`nombre`	string NOT NULL,
	`precio`	REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS "clientes" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`nombre`	string NOT NULL,
	`numero_documento`	string NOT NULL
);
CREATE TABLE `pedidos_clientes` (
	`Field1`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`id_cliente`	INTEGER NOT NULL,
	`id_usuario`	INTEGER NOT NULL,
	`fecha`	date,
	FOREIGN KEY(`id_cliente`) REFERENCES `clientes`(`id`),
	FOREIGN KEY(`id_usuario`) REFERENCES `usuarios`(`id`)
);
CREATE TABLE IF NOT EXISTS "usuarios" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`nombre`	string NOT NULL UNIQUE,
	`contrasena`	string NOT NULL,
	`activo`	boolean DEFAULT 1
);
INSERT INTO "usuarios" VALUES(1,'admin','admin',1);
INSERT INTO "usuarios" VALUES(2,'chepe',123,0);
INSERT INTO "usuarios" VALUES(3,'test','test',1);
INSERT INTO "usuarios" VALUES(4,'caca',456,0);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('clientes',0);
INSERT INTO "sqlite_sequence" VALUES('sistema_pagos',4);
INSERT INTO "sqlite_sequence" VALUES('usuarios',4);
COMMIT;
