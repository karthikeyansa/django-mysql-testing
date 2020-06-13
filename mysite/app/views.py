from django.shortcuts import render,redirect
from .models import Test
# Create your views here.
def testing(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        data = Test(name = name,age = age)
        data.save()
        return redirect(testing)
    datas = Test.objects.all()
    return render(request,'mysite/index.html',{'datas':datas})
def delete(request ,id):
    test = Test.objects.get(id = id).delete()
    return redirect(testing)


