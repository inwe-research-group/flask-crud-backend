# Descargar el proyecto desde github
1.Descargar el proyecto desde github
2.cree el archivo .env localmente con los parametros de conexion a la base de datos
# Levantar el proyecto en ambiente local
Para ingresar al entorno virtual:
desde la ruta del proyecto lanzar el siguiente comando:

virtualenv venv

para activar el entorno virtual, desde la ruta del proyecto lanzar el siguiente comando:
venv\Scripts\activate

una vez activado el entorno virtual debe mostrar como se indica:
(venv) PS C:\RutaDelProyecto

luego lanzar la instruccion para instalar las dependencias:
pip install -r requirements.txt

para desplegar en ambiente local:
python app.py runserver

# Endpoints:
_____________
> get Contactos :  METHOD: GET http://127.0.0.1:5002
_____________
> Nuevo Contacto : METHOD POST http://127.0.0.1:5002/new
body:
{   
    "fullname": "Mick Jagger",
    "email": "jagger@gmail.com",    
    "phone": "65656565"
}

> Modificar Contacto : METHOD POST http://127.0.0.1:5002/update
body:
{    
    "id": 30,
    "fullname": "Tina Tuner",
    "email": "tuner@gmail.com",    
    "phone": "52525252"
}

> Eliminar Contacto : METHOD POST http://127.0.0.1:5002/delete
body:
{
    "id": 30
}

