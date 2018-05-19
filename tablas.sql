PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE `usuarios` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`nombre`	string NOT NULL UNIQUE,
	`contrasena`	string NOT NULL
);
INSERT INTO "usuarios" VALUES(1,'esteban','esteban');
INSERT INTO "usuarios" VALUES(2,'chepe','chepe');
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
CREATE TABLE `servicios` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`codigo`	string NOT NULL UNIQUE,
	`nombre`	string NOT NULL,
	`precio`	REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS "clientes" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`nombres`	string NOT NULL,
	`numero_documento`	string NOT NULL
);
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('usuarios',2);
INSERT INTO "sqlite_sequence" VALUES('clientes',0);
COMMIT;
