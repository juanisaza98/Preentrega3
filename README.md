# Proyecto coderhouse

Comision: 54135

Alumno: Juan Manuel Isaza Giraldo

# Acerca del proyecto
Entrega final enfocada en los siguientes items.

🕵️ Cumplimiento de consigna:

💫 Entrega hecha por GitHub

💫 Readme con la explicación del proyecto

💫 Video de no más de 10 minutos

https://youtu.be/-xlEOlAghJM

🕵️ Estructura interna:

💫 una o más aplicaciones creadas

💫 dos modelos con campos de texto, número, fecha

💫 vista de listado de registros de un modelo

💫 vista del detalle de un registro de un modelo

💫 vista para crear un registro de un modelo

💫 vista para eliminar un registro de un modelo

💫 about/ que hable sobre el creador del proyecto

🕵️ Lógica de usuarios:

💫 login de usuario

💫 registro de usuario

💫 administrador: puede realizar CRUD sobre los modelos

💫 administrador: subir una imagen de perfil para un usuario

🕵️ Flujo del proyecto

💫 Ingresar a la web app desde la ruta base ‘/’ y direccionar a “home”

💫 navegar entre las diferentes URL sin tener que usar la “barra del navegador”


Inicio de ecommerce para emprendimiento de Dips

Pestana Home: Presenta imagen, boton de whatsapp y navbar con diferentes opciones dependiendo si estas logueado, y si eres usuario normal o staff


# Comandos

`mkdir nueva_carpeta`
> Crea una carpeta llamada nueva_carpeta

`ls`
> Muestra la lista de archivos

`cd nueva_carpeta`
> Cambia de carpeta

`pwd`
> Muestra la ruta actual

`python -m venv .venv`
> Crea un entorno virtual llamado .venv

`source .venv/bin/activate`
> Activa el entorno virtual en Linux o Mac

`.\venv\Scripts\activate`
> Activa el entorno virtual en Windows

`pip list`
> Muestra la lista de paquetes disponibles en el entorno virtual

`pip install django`
> Instala Django

`django-admin startproject config .`
> Crea un proyecto en el directorio actual

`python manage.py runserver`
> Ejecuta el servidor

`python manage.py startapp app`
> Crea una nueva aplicación llamada app

`python manage.py makemigrations`
> Crea las migraciones, que son archivos Python encargados de la base de datos

`python manage.py migrate`
> Ejecuta las migraciones, para que se realicen los cambios en la base de datos

`python manage.py createsuperuser`
> Crea un usuario administrador para acceder a 127.0.0.1:8000/admin

## Crear archivo de requisitos: requirements.txt

`pip freeze >> requirements.txt`
`pip install -r requirements.txt`

# Aplicaciones
Ecommerce

# Modelos
Clientes
Productos
Pedido

# Mejoras futuras
Se pretende mejorar la visualizacion de la pagina, con colores que tengan mas coherencia con los colores de la marca

Mejora en las dinamicas de la pagina, con mas imagenes y mas interaccion con el usuario

Se pretende agregar "Carrito de mercado" para compras de varios productos

Agregar funciones de pago en linea

Terminar CRUD para clientes y pedidos

Cambio de plantilla de bootstrap

