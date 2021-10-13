from django.contrib import admin
from shopitapp.models import *

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_editable = ['price']
    prepopulated_fields = {
        'slug': ['title']
    }


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Condition)
admin.site.register(Screensize)
admin.site.register(Operating_system)
admin.site.register(Color)
admin.site.register(Ram)
admin.site.register(Storage)
admin.site.register(Product, ProductAdmin)
admin.site.register(FeaturedProduct)
admin.site.register(Leaderboard)
admin.site.register(Display)
admin.site.register(FrontCamera)
admin.site.register(BackCamera)
