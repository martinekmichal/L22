from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ("Název", "Autor", "Rok",)


admin.site.register(Member, MemberAdmin)

