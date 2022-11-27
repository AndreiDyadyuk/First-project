from datetime import datetime
from django.shortcuts import render, redirect
from .models import Product, Comments
from .forms import Comment


def products(request) :

    all_products = Product.objects.all()
    return render(request, 'products.html', {'products': all_products})


def contacts(request) :

    return render(request, 'contacts.html')



def product(request, id) :

    product = Product.objects.get(id=id)
    return render(request, 'product.html', {'product': product})


def all_com(request) :

    all_com = Comments.objects.all().order_by('-issued')
    return render(request, 'comments.html', {'all_com':all_com})

def com(request, id) :

    com = Comments.objects.get(id=id)
    return render(request, 'comment.html', {'com':com})


def add_comment(request) :
    
    if request.method == 'POST' :
        form = Comment(request.POST, request.FILES)

        if form.is_valid() :
            comment = Comments()
            comment.issued = datetime.now()
            comment.name = form.cleaned_data['name']
            comment.comment = form.cleaned_data['comment']
            comment.save()

            return redirect('all_com')

    else :
        form = Comment()        

    return render(request, 'add_comment.html', {'form': form})






