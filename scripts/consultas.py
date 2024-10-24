from django.db.models import Count, Sum, F
from app.models import Tarea, Epica, Sprint, User

# 1. Obtener todas las tareas asignadas a un usuario especifico
usuario = User.objects.get(username='usuario1')  
tareas_usuario = Tarea.objects.filter(responsable=usuario)

# 2. Obtener las tareas completadas dentro de un sprint determinado
sprint = Sprint.objects.get(nombre='Sprint 1')  
tareas_completadas_sprint = Tarea.objects.filter(sprint_asignado=sprint, estado='COMPLETADA')

# 3. Listar todas las tareas que dependen de una tarea especifica
tarea_especifica = Tarea.objects.get(titulo='Tarea 1') 
dependencias_tarea = tarea_especifica.dependencias.all()

# 4. Listar todas las épicas que tienen tareas en progreso
epicas_con_tareas_en_progreso = Epica.objects.filter(tareas_asociadas__estado='EN_PROGRESO').distinct()

# 5. Calcular el número total de tareas por estado (por hacer, en progreso, completada)
tareas_por_estado = Tarea.objects.values('estado').annotate(total=Count('id'))

# 6. Obtener la suma de esfuerzo estimado de todas las tareas asociadas a una épica específica.
epica = Epica.objects.get(nombre='Desarrollo de módulo de autenticación')  
suma_esfuerzo_epica = epica.tareas_asociadas.aggregate(total_esfuerzo=Sum('esfuerzo_estimado'))

# 7. Listar los sprints que tiene un Scrum Master asignado.
sprints_con_scrum_master = Sprint.objects.filter(scrum_master__isnull=False)

# 8. Obtener el progreso total de una épica en base a las tareas completadas.
progreso_total_epica = epica.tareas_asociadas.aggregate(progreso_total=Sum('estado', filter=Q(estado='COMPLETADA')))

# 9. Obtener el backlog de un sprint específico y sus responsables.
backlog_sprint = Sprint.objects.filter(nombre='Sprint 1').prefetch_related('backlog_sprint') 

# 10. Listar todas las tareas que están bloqueadas.
tareas_bloqueadas = Tarea.objects.filter(bloqueadores__isnull=False)


print("Tareas asignadas a usuario:", tareas_usuario)
print("Tareas completadas en el sprint:", tareas_completadas_sprint)
print("Dependencias de la tarea específica:", dependencias_tarea)
print("Épicas con tareas en progreso:", epicas_con_tareas_en_progreso)
print("Número total de tareas por estado:", tareas_por_estado)
print("Suma de esfuerzo estimado en la épica:", suma_esfuerzo_epica)
print("Sprints con Scrum Master asignado:", sprints_con_scrum_master)
print("Progreso total de la épica:", progreso_total_epica)
print("Backlog del sprint:", backlog_sprint)
print("Tareas bloqueadas:", tareas_bloqueadas)

