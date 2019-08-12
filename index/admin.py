from django.contrib import admin
from .models import *
# Register your models here.


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'isActive']
    list_editable = ['description']
    search_fields = ['name', 'price']
    list_filter = ['name', 'price']


admin.site.register(Goods,GoodsAdmin)
admin.site.register(GoodsType)
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Banner)
admin.site.register(Ad)



