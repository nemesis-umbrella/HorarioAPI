--
-- volcado de datos para la tabla 'api_estado'
--
INSERT INTO api_estado VALUES (1,'Activo');
INSERT INTO api_estado VALUES (2,'Inactivo');

--
-- volcado de datos para la tabla 'api_estado'
--
INSERT INTO api_carrera VALUES ('INFO','Informática');
INSERT INTO api_carrera VALUES ('SIST','Sistemas computacionales');
INSERT INTO api_carrera VALUES ('CONTA','Contaduria');
INSERT INTO api_carrera VALUES ('GESTE','Gestión empresarial');
INSERT INTO api_carrera VALUES ('QUIM','Química');
INSERT INTO api_carrera VALUES ('BQUIM','Bioquímica');
INSERT INTO api_carrera VALUES ('AERO','Aeronáutica');

--
-- volcado de datos para la tabla 'api_materia'
--
INSERT INTO api_materia (nombre,creditos) VALUES ('Fundamentos de programación',5);
INSERT INTO api_materia (nombre,creditos) VALUES ('Programamación orienteda a objetos',5);
INSERT INTO api_materia (nombre,creditos) VALUES ('Fundamentos de base de datos',4);
INSERT INTO api_materia (nombre,creditos) VALUES ('Algebra lineal',5);
INSERT INTO api_materia (nombre,creditos) VALUES ('Fundamentos de redes',4);
INSERT INTO api_materia (nombre,creditos) VALUES ('Administración',3);

--
-- Volcado de datos para la tabla 'api_profesor'
--
INSERT INTO api_profesor VALUES(6789512,'Jill', 'Valentine',1);
INSERT INTO api_profesor VALUES(8964481,'Chris', 'Redfield',1);
INSERT INTO api_profesor VALUES(5964412,'Albert', 'Wesker',1);
INSERT INTO api_profesor VALUES(1291564,'Claudia', 'Morán',1);
INSERT INTO api_profesor VALUES(2015544,'José', 'Limón',1);

--
-- Volcado de datos para la tabla 'api_alumno'
--
INSERT INTO api_alumno VALUES (201450484,'Jorge L.', 'Mondragón','INFO',1);
INSERT INTO api_alumno VALUES (201459920,'Daniel', 'Peréz','SIST',1);
INSERT INTO api_alumno VALUES (201455699,'Alexa', 'Reyes','BQUIM',1);
INSERT INTO api_alumno VALUES (201446462,'Nancy', 'Zepeda','GESTE',1);
INSERT INTO api_alumno VALUES (201445897,'Juan', 'Sanachez','AERO',1);
