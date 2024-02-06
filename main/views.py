from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render

from main.models import Car, Client, Sale

def cars_list_view(request):
    search_input = request.GET.get('q')
    search_param = search_input if search_input != None else ''
    # получите список авто
    # car_list = Car.objects.all()
    car_list = Car.objects.filter(model__icontains=search_param)
    template_name = 'main/list.html'
    context = {'cars': car_list}
    return render(request, template_name, context=context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404

    try:
        car = Car.objects.get(id=car_id)
        template_name = 'main/details.html'
        context = {'car': car}
        return render(request, template_name, context=context)  # передайте необходимый контекст
    except:
        return HttpResponseNotFound('Car not found')


def sales_by_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        sales = Sale.objects.filter(car=car_id)
        # получите авто и его продажи
        template_name = 'main/sales.html'
        context = {
            'car': car,
            'sales': sales
        }
        return render(request, template_name, context=context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
