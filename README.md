# Books Foro 
Aplicativo de prueba para un reclutador en el que se solicitaba el desarrollo de una aplicación donde se demostrara destreza con la creación, manejo y consumos de API tanto externas como internas con un framework de Python y con esto utilizar las librerías necesarias para generar reportes en pdf y xlsx.

## Entorno en el que fue desarrollado;

* [x]  Sistema operativo Ubuntu 20.04 LTS
* [x]  Motor de bases de datos sqlite 3.31.1
* [x]  Python 3.8.2

## Stack Tecnológico

### Para frontend se utlizó:
* [x] html5 
* [x] css3
* [x] js 
* [x] jquery(Enlazado externamente)

### Para backend se utilizaron las siguientes librerías
* [x] flask
* [x] sqlalchemy
* [x] flask-cors
* [x] openpyxl
* [x] reportalab

###  Las librerías se instalan de la siguiente forma:

pip install -r requirements.txt

## La aplicación funciona de la siguiente manera:

### 1ro 
- Abrir una terminal y ubicarse en la carpeta raíz de la aplicación "intellinext". 
  Ejecutar el comando: python3 app.py

### 2do
 - Abrir otra terminal y ubicarse en la carpeta raíz de la aplicación. 
   Ejecutar el comando: python3 -m api.v1.main 

### 3ro
- En el navegador digitar la url: http://localhost:5000/  este lo redirigirá al login, aquí ya se puede registrar y hacer uso de la aplicación

## API para reportes

Los datos de los reportes provienen de la API pública de https://openlibra.com/
