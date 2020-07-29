# Horario - API

_Sistema para tomar asistencias de los alumnos, incluye sitio web para administrar y visualizar las asistencias, así como una API para su implementación en otra plataforma._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

* Python 3.6.9 o superior, se puede descargar de [aquí](https://www.python.org/)
* [PostgreSQL](https://www.postgresql.org/) 10.12 o superior (Opcional) *
* [Django](https://www.djangoproject.com/) versión 3.0.8
    
    Linux:
    ```
    pip3 install Django==3.0.8
    ```

    Windows:
    ```
    pip install Django==3.0.8
    ```
* Django REST framework ([djangorestframework](https://www.django-rest-framework.org/))

    Linux:
    ```
    pip3 install djangorestframework
    ```

    Windows:
    ```
    pip install djangorestframework
    ```
* [Psycopg](https://www.psycopg.org/) - PostgreSQL driver for Python (Opcional) *
  
  Linux:
  ```
  pip3 install psycopg2
  ```
  
  Windows:
  ```
  pip install psycopg2
  ```
* Django crontab ([django-crontab](https://pypi.org/project/django-crontab/))
    
    Linux:
    ```
        pip3 install django-crontab
    ```
    Windows:
    ```
        pip install django-crontab
    ```
(*) Solo en caso de querer utilizar otro gestor de base de datos, o en su defecto la versión local del proyecto.
### Instalación 🔧

_A continuación se explica como debes instalar el proyecto para tener un entorno de desarrollo y poder utilizarlo._

_En caso de no utilizar PostgreSQL y el backup localizado en el proyecto, deben realizarse los siguientes pasos. Previo necesario configurar los drives correspondientes en el archivo settings del proyecto ([información aqui](https://docs.djangoproject.com/en/3.0/ref/databases/))._

Migración de los modelos del proyecto a la base de datos (Solo en caso de no utilizar el backup). 

```
Desde la terminal, en la ruta del proyecto ejecutar la siguiente línea.

python3 manage.py migrate
```
Creación de superusuario, para administrar el sitio
```
python3 manage.py createsuperuser
```
 **Nota:** En caso de decidir empezar con un proyecto en blanco, es necesario que se creen los datos de forma manual para cada uno de los modelos. 

_Configuración de procesos en segundo plano (necesarios para realizar el cierre de las asistencias)_

```
Desde la terminal ejecutar la siguiente sentencia, para dar de alta los jobs

    python3 manage.py crontab add
    
Una vez hecho esto se comprueba utilizando la siguiente sentencia

    python3 manage.py crontab show
    
```

_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_

## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_
* [Visual Studio Code](https://code.visualstudio.com/) - Edición de código. Redefinido.
* [Django](https://www.djangoproject.com/) - El marco web para perfeccionistas con plazos.

* [pgAdmin](https://www.pgadmin.org/download/) - La plataforma de administración y desarrollo de código abierto más popular y rica en características para PostgreSQL.

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Jorge L. Mondragón** - *Trabajo Inicial* - [nemesis-umbrella](https://github.com/nemesis-umbrella)
* **Álvaro Velasco** - *Documentación* - [AlvaroIVC](https://github.com/AlvaroIVC)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (MIT) - mira el archivo [LICENSE](LICENSE) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.



---
⌨️ con ❤️ por [Jorge L. Mondragón](https://github.com/nemesis-umbrella) 👾
