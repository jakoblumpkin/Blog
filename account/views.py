from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import redirect
from .models import thumbs, section
from .forms import commentForm
import datetime
# Create your views here.
def home(request):
    sec=section.objects.all()
    both=thumbs.objects.get(id=1)
    like=both.like
    dislike=both.dislike
    form=commentForm()
    context={"like":like, "dislike":dislike, "form":form, "sec":sec}
    return render(request, 'index.html', context)

def like(request):
    num=thumbs.objects.get(id=1)
    num.like+=1
    num.save()
    context = {"like": like, "dislike": dislike}
    return redirect('/')

def dislike(request):
    num=thumbs.objects.get(id=1)
    num.dislike+=1
    num.save()
    return redirect('/')

def comment(request):
    form=commentForm()
    if request.method=='POST':
        form=commentForm(request.POST)
        if form.is_valid():
            form.save()
            current=datetime.datetime.now()
            sec = section.objects.all()
            num = max([i.id for i in sec])
            obj=section.objects.get(id=num)
            obj.time=current
            obj.save()

            # ses=section.objects.all()
            # obj=ses
            # print(obj)




    return redirect('/')
