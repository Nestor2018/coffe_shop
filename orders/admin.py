from django.contrib import admin

from .models import Order, OrderProduct


class orderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [orderProductInlineAdmin]


admin.site.register(Order, OrderAdmin)
