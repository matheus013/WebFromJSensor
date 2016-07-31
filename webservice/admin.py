from django.contrib import admin
from webservice.models import Application
from webservice.models import Node
from webservice.models import StateApp
from webservice.models import Operation

admin.site.register(Node)
admin.site.register(StateApp)
admin.site.register(Application)
admin.site.register(Operation)
