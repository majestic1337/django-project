from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, DeleteView

from .forms import OrderForm, OrderFormEdit
from .models import Order


# Create your views here.
def orders(request):
    order = Order.objects.all()

    # Отримання унікальних значень наповнювачів з бази даних

    return render(request, 'order/orders.html', {'orders': order})

def orders_detail_view(request,order_id):
    order= get_object_or_404(Order, pk=order_id)
    return render(request, 'order/order_details.html', {'orders': order})

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = OrderForm()

    return render(request, 'order/buy.html', {'form': form})

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order/buy.html'
    form_class=OrderFormEdit

class OrderDeleteView(DeleteView):
    model = Order
    success_url = '/'
    template_name = 'order/order_delete.html'
