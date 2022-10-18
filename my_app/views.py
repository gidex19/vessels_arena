from django.shortcuts import get_object_or_404, render
from .models import Customuser, Devotional
from django.http import JsonResponse, HttpResponse
# from .forms import AddForm
# Create your views here.


def home(request):
    print(request)
    return render(request, 'my_app/home.html')
    # return HttpResponse("<h1>Response html</h1>")
    # return JsonResponse({'name': 'hello name'})

def branches(request):
    return render(request, 'my_app/branches.html')

# def addformpage(request):
#     form = AddForm()

#     return render(request, 'my_app/add_form.html', { 'form': form})

def about(request):
    return render(request, 'my_app/about.html')

def devotional(request):
    all_devotional = Devotional.objects.all()
    context = {'all_devotional': all_devotional}
    return render(request, 'my_app/devotional.html', context)

def devotional_detail(request, pk):
    all_devotional = Devotional.objects.all()
    devotional = get_object_or_404(Devotional, pk= pk)
    context = {'devotional': devotional, 'all_devotional': all_devotional}
    return render(request, 'my_app/devotional_detail.html', context)

def history(request):
    return render(request, 'my_app/history.html')    

def vision(request):
    return render(request, 'my_app/vision.html')    

def message(request):
    return render(request, 'my_app/message.html')  

def sfw(request):
    return render(request, 'my_app/sfw.html')  

def men_of_valour(request):
    return render(request, 'my_app/men_of_valour.html')  

def tender_vessels(request):
    return render(request, 'my_app/tender_vessels.html')  


