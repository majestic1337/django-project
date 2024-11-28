from django.shortcuts import render, get_object_or_404, redirect
from .forms import CandyForm
from .models import Desert, Filling
from django.views.generic import UpdateView,DeleteView


# Create your views here.

def catalog(request):
    candies = Desert.objects.all()

    # Отримання унікальних значень наповнювачів з бази даних
    fillings = Filling.objects.all()

    sorting = request.GET.get('sorting')
    desired_id = None

    for filling in fillings:
        if filling.name == sorting:
            desired_id = filling.id
            break  # Якщо знайдено відповідний запис, припиняємо перебір

    if sorting and sorting != 'all':
        candies = candies.filter(filling=desired_id)

    return render(request, 'deserts/catalog.html', {'candies': candies, 'fillings': fillings})


def add_candy(request):
    if request.method == 'POST':
        form = CandyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CandyForm()

    return render(request, 'deserts/create.html', {'form': form})


def candy_detail_view(request, candy_id):
    candy = get_object_or_404(Desert, pk=candy_id)
    fillings = Filling.objects.all()
    return render(request, 'deserts/candy_detail.html', {'candy': candy, 'fillings': fillings})

class CandyUpdateView(UpdateView):
    model = Desert
    template_name = 'deserts/create.html'
    form_class=CandyForm

class CandyDeleteView(DeleteView):
    model = Desert
    success_url = '/'
    template_name = 'deserts/candy_delete.html'

