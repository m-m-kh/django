from django.shortcuts import render
from . import models

def note_list(request):
    
    
    context = {
        "data":models.Note.objects.all()
    }
    
    return render(request, 'index.html',
                  context=context)