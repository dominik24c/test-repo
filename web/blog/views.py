from django.shortcuts import render,redirect

from blog.forms import BlogForm

# Create your views here.

def create_blog(request):
    context={}

    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm()
    
    context['form']=form
    return render(request,'blog/create.html',context)