-- SQLite
--
-- Creación de la BD s_asistencia
--
-- Creación de tablas catalogo
--
CREATE TABLE ct_estado(
    id_estado         INTEGER PRIMARY KEY,
    descripcion       VARCHAR(50)
);
CREATE TABLE ct_carrera(
    clave_carrera     CHAR(5) PRIMARY KEY,
    descripcion       VARCHAR(50)
);

CREATE TABLE ct_materia(
    id_materia      INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre          VARCHAR(50),
    creditos        INTEGER
);

--
-- Creación de tablas 
--
CREATE TABLE dt_profesor(
    clave_empleado  NUMERIC(10) PRIMARY KEY,
    nombre          VARCHAR(50),
    apellidos       VARCHAR(100),
    id_estado       INTEGER,
    CONSTRAINT fk_estado_prof FOREIGN KEY(id_estado) REFERENCES ct_estado(id_estado)
);

CREATE TABLE dt_alumno(
  matricula NUMERIC(11) PRIMARY KEY,
  nombre varchar(50),
  apellidos varchar(100),
  id_estado INTEGER,
  clave_carrera CHAR(5),
  CONSTRAINT fk_estado_alum FOREIGN KEY(id_estado) REFERENCES ct_estado(id_estado),
  CONSTRAINT fk_carrera_alum FOREIGN KEY(clave_carrera) REFERENCES ct_carrera(clave_carrera)
);

--
-- Creación de tablas intermedias
--
CREATE TABLE dt_carrera_materia(
    clave_carrera       CHAR(5),
    id_materia          INTEGER,
    CONSTRAINT UC_car_mat UNIQUE (clave_carrera,id_materia),
    CONSTRAINT fk_carrera_clave FOREIGN KEY (clave_carrera) REFERENCES ct_carrera(clave_carrera),
    CONSTRAINT fk_carrera_materia FOREIGN KEY (id_materia) REFERENCES ct_materia(id_materia)
);

CREATE TABLE dt_materia_profesor(
    id_mat_prof         INTEGER PRIMARY KEY AUTOINCREMENT,
    id_materia          INTEGER,
    clave_empleado      NUMERIC(10),
    CONSTRAINT UC_materia_prof UNIQUE(id_materia,clave_empleado),
    CONSTRAINT fk_materia_prof FOREIGN KEY(id_materia) REFERENCES ct_materia(id_materia),
    CONSTRAINT fk_materia_prof_cve FOREIGN KEY(clave_empleado) REFERENCES dt_profesor(clave_empleado)
);

CREATE TABLE dt_clase_horario(
    id_clase_horario    INTEGER PRIMARY KEY AUTOINCREMENT,
    id_mat_prof         INTEGER,
    lun_ini             TIME,
    lun_fin             TIME,
    mar_ini             TIME,
    mar_fin             TIME,
    mie_ini             TIME,
    mie_fin             TIME,
    jue_ini             TIME,
    jue_fin             TIME,
    vie_ini             TIME,
    vie_fin             TIME,
    sab_ini             TIME,
    sab_fin             TIME,
    id_estado           INTEGER,
    CONSTRAINT fk_cls_hor_mat_prof FOREIGN KEY(id_mat_prof) REFERENCES dt_materia_profesor(id_mat_prof),
    CONSTRAINT fk_estado_clase_horario FOREIGN KEY(id_estado) REFERENCES ct_estado(id_estado)
);

CREATE TABLE dt_alum_clase_horario(
    id_alum_clas_hor    INTEGER PRIMARY KEY AUTOINCREMENT,
    matricula           NUMERIC(11),
    id_clase_horario    INTEGER,
    id_estado           INTEGER,
    CONSTRAINT fk_alum_horario FOREIGN KEY(matricula) REFERENCES dt_alumno(matricula) ON DELETE CASCADE,
    CONSTRAINT fk_alum_clas_horario FOREIGN KEY(id_clase_horario) REFERENCES dt_clase_horario(id_clase_horario),
    CONSTRAINT fk_estado_hor_alumn FOREIGN KEY(id_estado) REFERENCES ct_estado(id_estado)
);

CREATE TABLE dt_asistencia(
    no_asistencia       INTEGER PRIMARY KEY AUTOINCREMENT,
    id_alum_clas_hor    INTEGER,
    matricula           NUMERIC(11),
    fecha               DATE,
    hora_entrada        TIME,
    hora_salida         TIME,
    puntualidad         NUMERIC(1),
    CONSTRAINT fk_asist_alum_horario FOREIGN KEY(id_alum_clas_hor) REFERENCES dt_alum_clase_horario(id_alum_clas_hor),
    CONSTRAINT fk_asist_alum_matricula FOREIGN KEY(matricula) REFERENCES dt_alumno(matricula) ON DELETE CASCADE
);
--
-- volcado de datos para la tabla 'ct_estado'
--
INSERT INTO ct_estado VALUES (1,'Activo');
INSERT INTO ct_estado VALUES (2,'Inactivo');

--
-- volcado de datos para la tabla 'ct_estado'
--
INSERT INTO ct_carrera VALUES ('INFO','Informática');
INSERT INTO ct_carrera VALUES ('SIST','Sistemas computacionales');
INSERT INTO ct_carrera VALUES ('CONTA','Contaduria');
INSERT INTO ct_carrera VALUES ('GESTE','Gestión empresarial');
INSERT INTO ct_carrera VALUES ('QUIM','Química');
INSERT INTO ct_carrera VALUES ('BQUIM','Bioquímica');
INSERT INTO ct_carrera VALUES ('AERO','Aeronáutica');

--
-- volcado de datos para la tabla 'ct_materia'
--
INSERT INTO ct_materia (nombre,creditos) VALUES ('Fundamentos de programación',5);
INSERT INTO ct_materia (nombre,creditos) VALUES ('Programamación orienteda a objetos',5);
INSERT INTO ct_materia (nombre,creditos) VALUES ('Fundamentos de base de datos',4);
INSERT INTO ct_materia (nombre,creditos) VALUES ('Algebra lineal',5);
INSERT INTO ct_materia (nombre,creditos) VALUES ('Fundamentos de redes',4);
INSERT INTO ct_materia (nombre,creditos) VALUES ('Administración',3);

--
-- Volcado de datos para la tabla 'dt_profesor'
--
INSERT INTO dt_profesor VALUES(6789512,'Jill', 'Valentine',1);
INSERT INTO dt_profesor VALUES(8964481,'Chris', 'Redfield',1);
INSERT INTO dt_profesor VALUES(5964412,'Albert', 'Wesker',1);
INSERT INTO dt_profesor VALUES(1291564,'Claudia', 'Morán',1);
INSERT INTO dt_profesor VALUES(2015544,'José Luis', 'Limón',1);

--
-- Volcado de datos para la tabla 'dt_alumno'
--
INSERT INTO dt_alumno VALUES (201450484,'Jorge L.', 'Mondragón',1,'INFO');
INSERT INTO dt_alumno VALUES (201459920,'Daniel', 'Peréz',1,'SIST');
INSERT INTO dt_alumno VALUES (201455699,'Alexa', 'Reyes',1,'BQUIM');
INSERT INTO dt_alumno VALUES (201446462,'Nancy', 'Zavala',1,'GESTE');
INSERT INTO dt_alumno VALUES (201445897,'Juan', 'Sanchéz',1,'AERO');
