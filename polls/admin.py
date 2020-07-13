from django.contrib import admin

from .models import Fraga, Val

admin.site.site_header = "Medborgardialog Administration"
admin.site.site_title = "Medborgardialog Admin"
admin.site.index_title = "Välkommen till administrationspanelen"

class ValInLine(admin.TabularInline):
    model = Val
    extra = 2

class FragaAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['fraga_text']}),]
    inlines = [ValInLine]
# admin.site.register(Fraga)
admin.site.register(Val)
admin.site.register(Fraga, FragaAdmin)