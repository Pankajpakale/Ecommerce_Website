from django.contrib import admin
from app.models import Product,Customer,Cart

#Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','category','product_image']

admin.site.register(Product,ProductModelAdmin)

class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','state','pincode']

admin.site.register(Customer,CustomerModelAdmin)

class CartModeAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

admin.site.register(Cart,CartModeAdmin)
