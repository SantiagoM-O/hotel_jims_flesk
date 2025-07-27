#  Hotel JIMS - Aplicación de Reservas

Aplicación web desarrollada con **Flask** que permite a los clientes consultar habitaciones, realizar reservas, y a los administradores gestionar reservas de manera eficiente.

---

##  Funcionalidades principales

- **Página principal**  
  Presentación del hotel, imágenes y navegación a las diferentes secciones.

- **Reserva de habitaciones**  
  Consultar disponibilidad, calcular precio según fecha y tipo de habitación, y completar el formulario.

- **Almacenamiento**  
  Las reservas se guardan en un archivo `clientes.json` con formato estructurado.

- **Búsqueda de clientes**  
  Permite buscar por nombre, correo o rango de fechas.

- **Panel de administración**  
  Acceso restringido mediante usuario y contraseña para gestionar reservas.

- **Eliminación de reservas**  
  Los administradores pueden borrar reservas existentes.

- **Secciones adicionales**  
  Galería de imágenes, detalles de habitaciones y más.

---

## 🔧 Tecnologías utilizadas

| Categoría   | Herramienta/Framework     |
|-------------|---------------------------|
| Backend     | Flask (Python)            |
| Frontend    | HTML5, CSS3, JavaScript   |
| UI/UX       | Flatpickr (selector de fechas) |
| Persistencia| JSON (`clientes.json`)    |
| Templates   | Jinja2                    |

---

##  Flujo de usuario

1. El usuario accede a la página principal.
2. Consulta disponibilidad y calcula el valor de la reserva.
3. Completa y envía el formulario.
4. Los datos se validan y almacenan en `clientes.json`.
5. El administrador accede al panel, consulta registros o elimina reservas.

---

##  Seguridad

- Acceso al panel protegido mediante usuario y contraseña.
- Validación de datos en **frontend y backend**.

---

## 📎 Acceso al Proyecto

El proyecto Hotel JIMS se encuentra disponible tanto en su repositorio de GitHub como desplegado públicamente en línea para pruebas y navegación.

Repositorio en GitHub
- https://github.com/SantiagoM-O/hotel_jims_flesk

Proyecto en línea (Render.com)
- https://hotel-jims-flask.onrender.com/
