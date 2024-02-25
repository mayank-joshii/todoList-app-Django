from django.shortcuts import render, HttpResponse
from home.models import Task
# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST.get('title')
        descp = request.POST.get('descp')
        print(title, descp)
        ins = Task(tasktitle=title, taskdescp=descp)
        ins.save()
        context = {'success': True}

    return render(request, 'index.html', context)

def tasks(request):
    alltasks = Task.objects.all()
    context = {'tasks':alltasks}
    # for item in alltasks:
        # print(item.tasktitle)
    return render(request, 'tasks.html', context)