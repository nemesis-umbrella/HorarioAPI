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
    id_materia      SERIAL PRIMARY KEY,
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
    id_mat_prof         SERIAL PRIMARY KEY,
    id_materia          INTEGER,
    clave_empleado      NUMERIC(10),
    CONSTRAINT UC_materia_prof UNIQUE(id_materia,clave_empleado),
    CONSTRAINT fk_materia_prof FOREIGN KEY(id_materia) REFERENCES ct_materia(id_materia),
    CONSTRAINT fk_materia_prof_cve FOREIGN KEY(clave_empleado) REFERENCES dt_profesor(clave_empleado)
);

CREATE TABLE dt_clase_horario(
    id_clase_horario    SERIAL PRIMARY KEY,
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
    id_alum_clas_hor    SERIAL PRIMARY KEY,
    matricula           NUMERIC(11),
    id_clase_horario    INTEGER,
    id_estado           INTEGER,
    CONSTRAINT fk_alum_horario FOREIGN KEY(matricula) REFERENCES dt_alumno(matricula) ON DELETE CASCADE,
    CONSTRAINT fk_alum_clas_horario FOREIGN KEY(id_clase_horario) REFERENCES dt_clase_horario(id_clase_horario),
    CONSTRAINT fk_estado_hor_alumn FOREIGN KEY(id_estado) REFERENCES ct_estado(id_estado)
);

CREATE TABLE dt_asistencia(
    no_asistencia       SERIAL PRIMARY KEY,
    id_alum_clas_hor    INTEGER,
    matricula           NUMERIC(11),
    fecha               DATE,
    hora_entrada        TIME,
    hora_salida         TIME,
    puntualidad         NUMERIC(1),
    CONSTRAINT fk_asist_alum_horario FOREIGN KEY(id_alum_clas_hor) REFERENCES dt_alum_clase_horario(id_alum_clas_hor),
    CONSTRAINT fk_asist_alum_matricula FOREIGN KEY(matricula) REFERENCES dt_alumno(matricula) ON DELETE CASCADE
);
