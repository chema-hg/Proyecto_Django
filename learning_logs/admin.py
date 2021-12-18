from django.contrib import admin

# Register your models here.
# Este código importa primero el módelo que queremos registrar Topic.
# El punto delante de models le dice a Django que busque models.py en el mismo directorio
# que admin.py
from .models import Topic
admin.site.register(Topic)
# le dice a Django que gestione nuestro modelo a través del sitio admin.

from .models import Entry
admin.site.register(Entry)