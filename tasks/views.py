from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Task

def index(request):
    latest_task_list = Task.objects.order_by('-created')
    context = {'latest_task_list': latest_task_list}
  
    if request.method == "POST":
        for task in context["latest_task_list"]:
            task_id = str(task.id)
            if request.POST.get("Remover" + task_id):
                task.delete()
            elif request.POST.get("check" + task_id):
                task.complete = True
                task.save()
            else:
                task.complete = False
                task.save()

        if 'title' in request.POST and request.POST['title']:
            new_task = Task(title=request.POST['title'], complete=False)
            new_task.save()

        return HttpResponseRedirect("/tasks/")
   
    return render(request, "tasks/index.html", context)