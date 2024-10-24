Proyecto Django - Gestión de Tareas, Épicas y Sprints

Este proyecto es una aplicación para la gestión ágil de proyectos, donde se modelan tareas, épicas y sprints. Permite administrar el ciclo de vida de las tareas, agruparlas en épicas y planificar su ejecución mediante sprints.
Modelos Principales
1. Tarea

El modelo Tarea representa una unidad de trabajo dentro del sistema. Los campos principales incluyen:

    titulo: Título de la tarea, un campo obligatorio de longitud máxima 200 caracteres.
    descripcion: Descripción de la tarea, también obligatoria.
    criterios_aceptacion: Criterios para la aceptación de la tarea, opcional.
    prioridad: Un número entero con un valor mínimo de 0.
    estado: Un campo de elección que puede ser POR_HACER, EN_PROGRESO o COMPLETADA.
    esfuerzo_estimado: Un número entero que representa el esfuerzo estimado de la tarea, con un valor mínimo de 0.
    responsable: Relación con el modelo User, puede ser nulo, lo que indica que no tiene un responsable asignado.
    sprint_asignado: Relación opcional con el modelo Sprint, que indica a qué sprint está asignada la tarea.
    dependencias: Relación con otras tareas, permitiendo definir tareas que dependen de otras.
    bloqueadores: Texto opcional que detalla los posibles impedimentos para la tarea.

El modelo incluye las siguientes restricciones de integridad:

    prioridad_no_negativa: Garantiza que la prioridad de la tarea sea igual o mayor a 0.
    esfuerzo_estimado_no_negativo: Garantiza que el esfuerzo estimado no sea negativo.
    estado_valido_tarea: Verifica que el estado de la tarea sea uno de los valores permitidos.

2. Sprint

El modelo Sprint representa un ciclo de trabajo en el que se planifican y completan tareas. Los campos incluyen:

    nombre: Nombre del sprint, obligatorio y de longitud máxima 200 caracteres.
    objetivo: Objetivo del sprint, obligatorio.
    fecha_inicio y fecha_fin: Fechas que indican el periodo de trabajo del sprint.
    velocidad: Número entero que mide la capacidad del equipo en términos de esfuerzo, con un valor mínimo de 0.
    scrum_master: Relación con User que indica quién es el Scrum Master del sprint.
    equipo_desarrollo: Relación ManyToMany con User, define los miembros del equipo de desarrollo.
    backlog_sprint: Relación ManyToMany con Tarea, contiene las tareas planificadas para ese sprint.

Restricciones:

    fecha_fin_posterior: Asegura que la fecha de fin del sprint sea posterior a la fecha de inicio.
    velocidad_no_negativa: Garantiza que la velocidad sea igual o mayor a 0.

3. Epica

El modelo Epica agrupa un conjunto de tareas relacionadas, generalmente representando una funcionalidad o un módulo dentro del sistema. Los campos incluyen:

    nombre: Título de la épica, obligatorio y de longitud máxima 200 caracteres.
    descripcion: Descripción de la épica, obligatoria.
    criterios_aceptacion: Criterios opcionales para definir cuándo la épica está completada.
    estado: Campo de elección con los valores POR_HACER, EN_PROGRESO y COMPLETADA.
    responsable: Relación con el modelo User que define quién es responsable de la épica.
    tareas_asociadas: Relación ManyToMany con Tarea, permitiendo asociar múltiples tareas a la épica.
    esfuerzo_estimado_total: Esfuerzo total estimado para completar la épica.
    fecha_inicio y fecha_fin: Fechas que definen el inicio y la finalización de la épica.
    progreso: Un valor flotante que va de 0 a 1, indicando el progreso de la épica en base a sus tareas completadas.

Restricciones:

    esfuerzo_total_no_negativo: Verifica que el esfuerzo total no sea negativo.
    progreso_valido: Garantiza que el progreso esté entre 0 y 1.
    estado_valido_epica: Asegura que el estado de la épica sea uno de los valores permitidos.
    fecha_fin_posterior_epica: Asegura que la fecha de fin sea posterior a la fecha de inicio.

Configuración y Ejecución del Proyecto
Requisitos

    Python 3.10
    Django 4.2

Instalación

    Clona el repositorio:


git clone <url-del-repositorio>

Instalar las dependencias del proyecto:

pip install -r requirements.txt

Ejecutar las migraciones:


python manage.py migrate

Crear un superusuario para acceder al panel de administración:


python manage.py createsuperuser

Ejecuta el servidor mediante:

    python manage.py runserver

    Acceder a 127.0.0.1:8000/admin/app/

Población y Borrado de Datos

Puedes poblar la base de datos con datos de ejemplo usando el script scripts_datos.py:

python manage.py shell < scripts_datos.py

Para borrar los datos creados en la base de datos, se facilito el script borrar_datos.py:
python manage.py shell < borrar_datos.py

Consultas y Agregaciones

El sistema permite realizar consultas utilizando relaciones y agregaciones entre los modelos. Algunas de las consultas que puedes realizar incluyen:

    Obtener todas las tareas asignadas a un usuario específico.
    Obtener las tareas completadas dentro de un sprint determinado.
    Listar todas las épicas que tienen tareas en progreso.
    Calcular el número total de tareas por estado (por hacer, en progreso, completada).
    Obtener la suma de esfuerzo estimado de todas las tareas asociadas a una épica.
    Listar los sprints que tienen un Scrum Master asignado.
    Obtener el progreso total de una épica en base a las tareas completadas.
    Obtener el backlog de un sprint específico y sus responsables.
