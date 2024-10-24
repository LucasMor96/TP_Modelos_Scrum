import random
from django.utils import timezone
from app.models import User, Tarea, Epica, Sprint


# Se crean los 10 usuarios
for i in range(1, 11):
    user = User.objects.create_user(
        username=f'usuario{i}', 
        email=f'usuario{i}@example.com', 
        password='contraseña123'
    )
    print(f'Usuario {user.username} creado')
    
# Los posibles valores para asignar con random
usuarios = list(User.objects.all())
prioridades = [1, 2, 3]  
esfuerzos = [3, 5, 8, 13, 21]  

# Se crean tres épicas
epica1 = Epica.objects.create(
    nombre="Desarrollo de módulo de autenticación",
    descripcion="Implementar un sistema de autenticación con Django",
    criterios_aceptacion="Debe soportar login, logout y registro de usuarios",
    estado='EN_PROGRESO',
    responsable=random.choice(usuarios),
    esfuerzo_estimado_total=random.choice(esfuerzos),
    fecha_inicio=timezone.now().date(),
    fecha_fin=timezone.now().date() + timezone.timedelta(days=45),
    progreso=0.5
)
epica2 = Epica.objects.create(
    nombre="Desarrollo de mòdulo de tareas",
    descripcion="Crear un módulo para gestionar tareas",
    criterios_aceptacion="Debe permitir crear, editar y eliminar tareas",
    estado='POR_HACER',
    responsable=random.choice(usuarios),
    esfuerzo_estimado_total=random.choice(esfuerzos),
    fecha_inicio=timezone.now().date(),
    fecha_fin=timezone.now().date() + timezone.timedelta(days=30),
    progreso=0.0
)
epica3 = Epica.objects.create(
    nombre="Optimización del rendimiento",
    descripcion="Optimizar consultas a la base de datos y mejorar la eficiencia",
    criterios_aceptacion="El tiempo de respuesta debe ser menor a 200ms",
    estado='EN_PROGRESO',
    responsable=random.choice(usuarios),
    esfuerzo_estimado_total=random.choice(esfuerzos),
    fecha_inicio=timezone.now().date(),
    fecha_fin=timezone.now().date() + timezone.timedelta(days=60),
    progreso=0.25
)

# Se crean tres sprints 
sprint1 = Sprint.objects.create(
    nombre="Sprint 1",
    objetivo="Completar la primera iteración",
    fecha_inicio=timezone.now().date(),
    fecha_fin=timezone.now().date() + timezone.timedelta(days=14),
    velocidad=30,
    scrum_master=random.choice(usuarios)
)

sprint2 = Sprint.objects.create(
    nombre="Sprint 2",
    objetivo="Optimización y refactorización del código",
    fecha_inicio=timezone.now().date(),
    fecha_fin=timezone.now().date() + timezone.timedelta(days=14),
    velocidad=25,
    scrum_master=random.choice(usuarios)
)

sprint3 = Sprint.objects.create(
    nombre="Sprint 3",
    objetivo="Desarrollo de nuevas características y pruebas finales",
    fecha_inicio=timezone.now().date(),
    fecha_fin=timezone.now().date() + timezone.timedelta(days=14),
    velocidad=35,
    scrum_master=random.choice(usuarios)
)

# Crear todas las tareas
# y se asignan a las épicas y a los sprints
for i in range(30):
    tarea = Tarea.objects.create(
        titulo=f"Tarea {i + 1}",
        descripcion=f"Descripción de la tarea {i + 1}",
        criterios_aceptacion="Debe cumplir con los requisitos de la historia de usuario",
        prioridad=random.choice(prioridades),
        estado=random.choice(['POR_HACER', 'EN_PROGRESO', 'COMPLETADA']),
        esfuerzo_estimado=random.choice(esfuerzos),
        responsable=random.choice(usuarios),
        sprint_asignado=random.choice([sprint1, sprint2, sprint3]),# Se asigna sprint aleatoriamente
        fecha_creacion=timezone.now(),
        fecha_actualizacion=timezone.now()
    )
    # Asignar cada tarea a una épica
    random.choice([epica1, epica2, epica3]).tareas_asociadas.add(tarea)

# Guardar todas las épicas después de asignar tareas
epica1.save()
epica2.save()
epica3.save()

