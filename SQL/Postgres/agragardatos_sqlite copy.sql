-- Postgres

-- Ingresar datos de materias asignadas a los profesores

INSERT INTO dt_materia_profesor(clave_empleado,id_materia) VALUES(6789512,1);
INSERT INTO dt_materia_profesor(clave_empleado,id_materia) VALUES(1291564,2);
INSERT INTO dt_materia_profesor(clave_empleado,id_materia) VALUES(8964481,3);
INSERT INTO dt_materia_profesor(clave_empleado,id_materia) VALUES(5964412,4);
INSERT INTO dt_materia_profesor(clave_empleado,id_materia) VALUES(2015544,5);
INSERT INTO dt_materia_profesor(clave_empleado,id_materia) VALUES(6789512,6);

-- Asignación de horarios a cada materia
INSERT INTO dt_clase_horario (id_mat_prof,lun_ini,lun_fin,mar_ini,mar_fin,mie_ini,mie_fin,jue_ini,jue_fin,vie_ini,vie_fin,sab_ini,sab_fin,id_estado) 
VALUES(2,'09:00:00','11:00:00',NULL,NULL,'11:00:00','13:00:00',NULL,NULL,'09:00:00','11:00:00',NULL,NULL,1);
INSERT INTO dt_clase_horario (id_mat_prof,lun_ini,lun_fin,mar_ini,mar_fin,mie_ini,mie_fin,jue_ini,jue_fin,vie_ini,vie_fin,sab_ini,sab_fin,id_estado)
VALUES(3,'11:00:00','13:00:00','09:00:00','11:00:00',NULL,NULL,'09:00:00','11:00:00',NULL,NULL,NULL,NULL,1);
INSERT INTO dt_clase_horario (id_mat_prof,lun_ini,lun_fin,mar_ini,mar_fin,mie_ini,mie_fin,jue_ini,jue_fin,vie_ini,vie_fin,sab_ini,sab_fin,id_estado)
VALUES(4,'13:00:00','15:00:00','11:00:00','13:00:00','09:00:00','11:00:00',NULL,NULL,NULL,NULL,NULL,NULL,1);
INSERT INTO dt_clase_horario (id_mat_prof,lun_ini,lun_fin,mar_ini,mar_fin,mie_ini,mie_fin,jue_ini,jue_fin,vie_ini,vie_fin,sab_ini,sab_fin,id_estado)
VALUES(5,NULL,NULL,'13:00:00','15:00:00',NULL,NULL,'11:00:00','13:00:00','13:00:00','14:00:00',NULL,NULL,1);
INSERT INTO dt_clase_horario (id_mat_prof,lun_ini,lun_fin,mar_ini,mar_fin,mie_ini,mie_fin,jue_ini,jue_fin,vie_ini,vie_fin,sab_ini,sab_fin,id_estado)
VALUES(6,NULL,NULL,NULL,NULL,'13:00:00','15:00:00','13:00:00','14:00:00','11:00:00','13:00:00',NULL,NULL,1);
INSERT INTO dt_clase_horario (id_mat_prof,lun_ini,lun_fin,mar_ini,mar_fin,mie_ini,mie_fin,jue_ini,jue_fin,vie_ini,vie_fin,sab_ini,sab_fin,id_estado)
VALUES(7,'15:00:00','17:00:00','15:00:00','17:00:00','15:00:00','17:00:00',NULL,NULL,NULL,NULL,NULL,NULL,1);

-- Asignación de horarios a alumnos
-- Alumno 1
INSERT INTO dt_alum_clase_horario(matricula,id_clase_horario,id_estado) VALUES(201450484,2,1);
INSERT INTO dt_alum_clase_horario(matricula,id_clase_horario,id_estado) VALUES(201450484,3,1);
INSERT INTO dt_alum_clase_horario(matricula,id_clase_horario,id_estado) VALUES(201450484,4,1);
INSERT INTO dt_alum_clase_horario(matricula,id_clase_horario,id_estado) VALUES(201450484,5,1);
INSERT INTO dt_alum_clase_horario(matricula,id_clase_horario,id_estado) VALUES(201450484,6,1);
INSERT INTO dt_alum_clase_horario(matricula,id_clase_horario,id_estado) VALUES(201450484,7,1);
-- Alumno 2
INSERT INTO dt_alum_clase_horario(matricula,id_clase_horario,id_estado) VALUES(201455699,2,1);
INSERT INTO dt_alum_clase_horario(matricula,id_clase_horario,id_estado) VALUES(201455699,3,1);
INSERT INTO dt_alum_clase_horario(matricula,id_clase_horario,id_estado) VALUES(201455699,4,1);
INSERT INTO dt_alum_clase_horario(matricula,id_clase_horario,id_estado) VALUES(201455699,5,1);
INSERT INTO dt_alum_clase_horario(matricula,id_clase_horario,id_estado) VALUES(201455699,6,1);
INSERT INTO dt_alum_clase_horario(matricula,id_clase_horario,id_estado) VALUES(201455699,7,1);

