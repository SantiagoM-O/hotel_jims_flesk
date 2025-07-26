Descripción General del Proyecto: Hotel JIMS


Este proyecto es una aplicación web de reservas para el Hotel JIMS, desarrollada con Flask (Python) como backend y HTML, CSS y JavaScript en el frontend. Permite a los usuarios consultar habitaciones, realizar reservas, y a los administradores gestionar y buscar clientes.



Funcionalidades principales


Página principal: Presenta el hotel, imágenes y acceso a las diferentes secciones.

Reserva de habitaciones: Los usuarios pueden consultar habitaciones disponibles, calcular el valor de la reserva según fechas y tipo de habitación, y completar un formulario para reservar.

Almacenamiento de reservas: Los datos de cada reserva se guardan en un archivo clientes.json en formato estructurado.

Búsqueda de clientes: Permite buscar clientes por nombre/correo o por rango de fechas de reserva.

Panel de administración: Acceso restringido mediante usuario y contraseña para consultar y eliminar reservas.

Eliminación de reservas: Los administradores pueden eliminar reservas de clientes.

Galería y otras secciones: Secciones adicionales como galería de imágenes y detalles de habitaciones.



Tecnologías utilizadas


Backend: Python (Flask)

Frontend: HTML5, CSS3, JavaScript (con Flatpickr para selección de fechas)

Persistencia: Archivo JSON (clientes.json)

Templates: Jinja2 para renderizado dinámico de páginas



Flujo básico de usuario


El usuario ingresa a la página principal y navega por las secciones.

Puede consultar habitaciones y calcular el valor de su reserva.

Completa el formulario de reserva, que se valida y guarda en el archivo JSON.

Un administrador puede acceder al panel, buscar reservas por nombre/correo o por fechas, y eliminar registros si es necesario.


Seguridad

Acceso al panel de administración protegido por usuario y contraseña.

Validación de datos en el frontend y backend.
