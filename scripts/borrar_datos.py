from app.models import Tarea, Epica, Sprint
from django.contrib.auth.models import User
from django.utils import timezone


Tarea.objects.all().delete()
print("Todas las tareas han sido eliminadas.")

Epica.objects.all().delete()
print("Todas las épicas han sido eliminadas.")


Sprint.objects.all().delete()
print("Todos los sprints han sido eliminados.")

User.objects.filter(username__startswith='usuario').delete()
print("Todos los usuarios han sido eliminados.")
