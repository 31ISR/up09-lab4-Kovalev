from django.shortcuts import render
from .models import Communities

def communities_list(request):
    communities = Communities.objects.all().order_by('-date')
    return render(request, 'communities/communities_list.html', {'communities': communities})

def communitie_page(request, slug):
    communitie = Communities.objects.get(slug=slug)  # исправлено имя переменной
    return render(request, 'communities/communitie_page.html', {'communitie': communitie})
