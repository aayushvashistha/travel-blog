from django.contrib import admin
from .models import blog, item, Subscriber
# Register your models here.

admin.site.register({blog, item, Subscriber})