from django.contrib import admin
from .models import User, Messages, Matches, Claims

# Register your models here.
admin.site.register(User)
admin.site.register(Messages)
admin.site.register(Matches)
admin.site.register(Claims)
