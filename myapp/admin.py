from django.contrib import admin
from .models import blog, item, Subscriber, write
# Register your models here.

admin.site.register({blog, item, Subscriber, write})