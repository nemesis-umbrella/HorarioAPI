-- SQLite
/*
SELECT * FROM ct_materia;
SELECT * FROM dt_profesor;
SELECT * FROM dt_materia_profesor;
SELECT * FROM dt_clase_horario;
SELECT * FROM dt_alumno;
SELECT * FROM dt_alum_clase_horario;
*/
-- Ingresar datos de materias asignadas a los profesores

INSERT INTO dt_materia_profesor VALUES(NULL,6789512,1);
INSERT INTO dt_materia_profesor VALUES(NULL,1291564,2);
INSERT INTO dt_materia_profesor VALUES(NULL,8964481,3);
INSERT INTO dt_materia_profesor VALUES(NULL,5964412,4);
INSERT INTO dt_materia_profesor VALUES(NULL,2015544,5);
INSERT INTO dt_materia_profesor VALUES(NULL,6789512,6);

-- Asignación de horarios a cada materia
INSERT INTO dt_clase_horario VALUES(NULL,1,'09:00:00','11:00:00',NULL,NULL,'11:00:00','13:00:00',NULL,NULL,'09:00:00','11:00:00',NULL,NULL,1);
INSERT INTO dt_clase_horario VALUES(NULL,2,'11:00:00','13:00:00','09:00:00','11:00:00',NULL,NULL,'09:00:00','11:00:00',NULL,NULL,NULL,NULL,1);
INSERT INTO dt_clase_horario VALUES(NULL,3,'13:00:00','15:00:00','11:00:00','13:00:00','09:00:00','11:00:00',NULL,NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO dt_clase_horario VALUES(NULL,4,NULL,NULL,'13:00:00','15:00:00',NULL,NULL,'11:00:00','13:00:00','13:00:00','14:00:00',NULL,NULL,1);
INSERT INTO dt_clase_horario VALUES(NULL,5,NULL,NULL,NULL,NULL,'13:00:00','15:00:00','13:00:00','14:00:00','11:00:00','13:00:00',NULL,NULL,1);
INSERT INTO dt_clase_horario VALUES(NULL,6,'15:00:00','17:00:00','15:00:00','17:00:00','15:00:00','17:00:00',NULL,NULL,NULL,NULL,NULL,NULL,1);

-- Asignación de horarios a alumnos
-- Alumno 1
INSERT INTO dt_alum_clase_horario VALUES(NULL,201450484,1,1);
INSERT INTO dt_alum_clase_horario VALUES(NULL,201450484,2,1);
INSERT INTO dt_alum_clase_horario VALUES(NULL,201450484,3,1);
INSERT INTO dt_alum_clase_horario VALUES(NULL,201450484,4,1);
INSERT INTO dt_alum_clase_horario VALUES(NULL,201450484,5,1);
INSERT INTO dt_alum_clase_horario VALUES(NULL,201450484,6,1);
-- Alumno 2
INSERT INTO dt_alum_clase_horario VALUES(NULL,201455699,1,1);
INSERT INTO dt_alum_clase_horario VALUES(NULL,201455699,2,1);
INSERT INTO dt_alum_clase_horario VALUES(NULL,201455699,3,1);
INSERT INTO dt_alum_clase_horario VALUES(NULL,201455699,4,1);
INSERT INTO dt_alum_clase_horario VALUES(NULL,201455699,5,1);
INSERT INTO dt_alum_clase_horario VALUES(NULL,201455699,6,1);

