from django.contrib import admin

from .models import category,product

# Register your models here.
class Category_admin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,Category_admin)
class product_admin(admin.ModelAdmin):
    list_display = ['name','price','stock','availability','created','updated']
    list_editable = ['price','stock','availability']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(product,product_admin)