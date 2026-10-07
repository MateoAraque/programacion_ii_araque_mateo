Programación II - Repositorio de Proyectos y Prácticas

Bienvenido al repositorio oficial de la asignatura Programación II. Este espacio está destinado a organizar los ejercicios, prácticas y proyectos desarrollados a lo largo del curso, abarcando desde fundamentos avanzados de programación hasta el desarrollo de aplicaciones web de nivel empresarial.

🛠️ Tecnologías Principales

En este curso se trabajará principalmente con el ecosistema de Python y sus frameworks más destacados para el desarrollo web y de sistemas de gestión ERP.

🐍 Python

Python es un lenguaje de programación multiparadigma, de alto nivel y de código abierto, reconocido por su sintaxis clara y legible. Es el pilar fundamental del curso, sirviendo de base para construir algoritmos, aplicar la Programación Orientada a Objetos (POO) y desarrollar aplicaciones robustas.

🌐 Django

Django es un framework de desarrollo web de alto nivel escrito en Python que fomenta un desarrollo rápido y un diseño limpio y pragmático. Basado en el patrón Model-Template-View (MTV), incluye de manera nativa un ORM para bases de datos, un panel de administración automático y mecanismos de seguridad listos para usar.

🏢 Odoo

Odoo es una suite de aplicaciones empresariales de código abierto (ERP/CRM) construida sobre Python y PostgreSQL. Permite crear y extender módulos de gestión de negocio (inventarios, contabilidad, ventas, etc.) utilizando una arquitectura basada en componentes y orientación a objetos.

📁 Estructura del Repositorio

El repositorio está organizado en carpetas y subcarpetas según las unidades o proyectos trabajados:

programacion-ii/
├── 01-python-avanzado/      # Ejercicios de POO, estructuras de datos y scripts
├── 02-django-proyectos/     # Aplicaciones y proyectos web desarrollados en Django
├── 03-odoo-modulos/        # Módulos personalizados y configuraciones de Odoo
├── docs/                    # Documentación adicional y guías
└── .gitignore               # Exclusión de entornos virtuales, caches y secretos



🚀 Requisitos Previos e Instalación

Clonar el repositorio:

git clone https://github.com/tu-usuario/programacion-ii.git
cd programacion-ii



Crear y activar un entorno virtual:

python -m venv venv
# En Linux/macOS:
source venv/bin/activate
# En Windows:
venv\Scripts\activate



Instalar dependencias generales:

pip install -r requirements.txt



📝 Buenas Prácticas

Mantener los entornos virtuales (venv/) e información sensible (.env) fuera del control de versiones (ver .gitignore).

Documentar las funciones y clases según las normas de estilo de Python (PEP 8).

Realizar commits claros y descriptivos al avanzar en cada módulo o práctica.