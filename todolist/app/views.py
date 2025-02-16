from django.shortcuts import render, redirect
from .models import To_do, To_do1
# Create your views here.
def To_do_list(request):
    if request.method == 'POST':
        task=request.POST.get('task')
        desc=request.POST.get('desc')
        To_do.objects.create(task=task,desc=desc)
        return redirect('home_name')
    return render(request,'to_do_list.html')
def home(request):
    if request.method == 'POST':
        a=request.POST.get('search')
        data=To_do.objects.filter(task__icontains=a)
    else:
       data=To_do.objects.all()
    context={
        'data':data
    }
    return render(request,'home.html',context)
def contact(request,pk):
    d1=To_do.objects.get(id=pk)
    if request.method == 'POST':
       To_do1.objects.create(task=d1.task, desc=d1.desc)
       d1.delete()
       return redirect('home_name')
    context={
        'd1':d1
    }
    return render(request,'contact.html',context)
def edit(request,pk):
    d2=To_do.objects.get(id=pk)
    if request.method == 'POST':
        task=request.POST.get('task')
        desc=request.POST.get('desc')
        d2.task=task
        d2.desc=desc
        d2.save()
        return redirect('home_name')
    context={
        'd2':d2
    }
    return render(request,'edit.html',context)

def history(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        data = To_do1.objects.filter(task__icontains=search)
    else:
        data = To_do1.objects.all()  # Fetch all tasks from To_do1 (History)

    context = {'data': data}
    return render(request, 'history.html', context)

def history_delete(request, pk):
    try:
        task = To_do1.objects.get(id=pk)  # Fetch task by ID
        task.delete()  # Permanently delete the task
        return redirect('history_name')  # Redirect back to the history page
    except To_do1.DoesNotExist:
        return redirect('history_name')  # If task not found, still redirect