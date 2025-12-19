from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    paginate_by = 5   # 👈 items per page

    def get_queryset(self):
        queryset = super().get_queryset().order_by("-id")
        query = self.request.GET.get("q")

        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "price"]
    template_name = "products/product_form.html"
    success_url = reverse_lazy("product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "price"]
    template_name = "products/product_form.html"
    success_url = reverse_lazy("product_list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/product_confirm_delete.html"
    success_url = reverse_lazy("product_list")

