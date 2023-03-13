from django.shortcuts import render
def jinga_print(request):
    d={'name':'ashu','age':8}
    return render(request,'jinga_print.html',context=d)

# Create your views here.
