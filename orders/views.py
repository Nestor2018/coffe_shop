from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import Order


class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).last()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        product_orders = order.orderproduct_set.all()

        # Calcula el total para cada producto
        for product_order in product_orders:
            product_order.total = product_order.product.price * product_order.quantity

        # Añade los product_orders al contexto
        context["product_orders"] = product_orders
        return context
