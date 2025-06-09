# ServiciosYa

ServiciosYa es una plataforma web desarrollada en Django que conecta consumidores con prestadores de servicios profesionales para el hogar y negocios. Permite la gestión integral de usuarios, servicios, contratos, pagos, facturación y calificaciones, facilitando la interacción segura y eficiente entre quienes buscan y quienes ofrecen servicios.

---

## Tabla de Contenidos

- [Características principales](#características-principales)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Instalación y configuración](#instalación-y-configuración)
- [Guía de uso](#guía-de-uso)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Contribución](#contribución)
- [Contacto](#contacto)

---

## Características principales

- **Registro y autenticación de usuarios** (consumidor y prestador)
- **Publicación y búsqueda de servicios** por categoría y localidad
- **Gestión de contratos** entre consumidores y prestadores
- **Pagos y facturación** integrados
- **Calificación y comentarios** sobre los prestadores
- **Paneles personalizados** para cada tipo de usuario
- **Gestión de direcciones** y ubicaciones
- **Administración completa** desde el panel de Django Admin

---

## Estructura del proyecto

El proyecto está organizado en varias aplicaciones Django, cada una con una responsabilidad clara:

- **apps/usuario**: Gestión de usuarios y roles (consumidor/prestador)
- **apps/servicio**: Servicios, categorías y servicios ofrecidos
- **apps/contrato**: Contratos entre usuarios
- **apps/pago**: Métodos y registros de pago
- **apps/facturacion**: Facturación de servicios
- **apps/ubicacion**: Provincias, localidades y direcciones
- **apps/calificacion**: Calificaciones y comentarios de usuarios

---

## Instalación y configuración

1. **Clona el repositorio**
    ```bash
    git clone https://github.com/tuusuario/serviciosya.git
    cd serviciosya
    ```

2. **Crea y activa un entorno virtual**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # En Windows
    ```

3. **Instala las dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configura la base de datos**
    - Edita `settings.py` con tus credenciales y preferencias.

5. **Aplica migraciones**
    ```bash
    python manage.py migrate
    ```

6. **Crea un superusuario**
    ```bash
    python manage.py createsuperuser
    ```

7. **Ejecuta el servidor**
    ```bash
    python manage.py runserver
    ```

---

## Guía de uso

- Accede a la plataforma en [http://localhost:8000](http://localhost:8000)
- Regístrate como consumidor o prestador.
- Los consumidores pueden buscar servicios, contratar, calificar y gestionar pagos.
- Los prestadores pueden publicar servicios, gestionar contratos y ver sus calificaciones.
- El panel de administración está disponible en `/admin` para la gestión avanzada.

---

## Tecnologías utilizadas

- **Backend:** Python 3, Django
- **Frontend:** HTML5, CSS3, Bootstrap, Django Templates
- **Base de datos:** SQLite (por defecto, puedes usar PostgreSQL/MySQL)
- **Otros:** Django Admin, sistema de autenticación personalizado

---

## Contribución

¿Quieres colaborar? ¡Eres bienvenido!

1. Haz un fork del repositorio.
2. Crea una rama para tu feature o fix: `git checkout -b mi-feature`
3. Realiza tus cambios y haz commit: `git commit -am 'Agrega nueva funcionalidad'`
4. Haz push a tu rama: `git push origin mi-feature`
5. Abre un Pull Request.

---

## Documentación Técnica

Consulta la [documentación técnica aquí](docs/tecnica.md).

---

## Contacto

Para soporte, sugerencias o consultas, puedes escribir a:

- **Email:** soporte@serviciosya.com
- **Equipo:** ServiciosYa

---

## Licencia

Este proyecto es de uso académico y privado. Para uso comercial, contacta al equipo de desarrollo.

---

¡Gracias por usar ServiciosYa!