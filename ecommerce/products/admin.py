from django.contrib import admin
from .models import Product, ProductCategory
# Register your models here.


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    ordering = ("name",)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock_quantity")
    search_fields = ("name", "category__name")
    list_filter = ("category",)
    ordering = ("name",)

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
