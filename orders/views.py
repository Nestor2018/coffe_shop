from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .models import Order
from .forms import OrderProductForm


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


class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy("my_order")

    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(is_active=True, user=self.request.user)
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)

