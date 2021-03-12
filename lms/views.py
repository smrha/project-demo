from django.shortcuts import render
from .forms import TermNewForm
from .models import Term

def index(request):
    return render(request, 'lms/index.html')

### TERM MODEL VIEWS ###

# List of all terms
def term_list(request):
    terms = Term.objects.all
    context = {
        'terms': terms
    }
    return render(request, 'lms/term/term-list.html', context)

# Adding a new term
def term_new(request):
    if request.method == 'POST':
        form = TermNewForm(request.POST)
        if form.is_valid():
            print(form.is_valid())
            form.save()
        # todo : else
    else:
        form = TermNewForm() 

    context = {
        'form': form
    }
    return render(request, 'lms/term/term-new.html', context)

# Editing the term
def term_edit(request, pk):
    obj = Term.objects.get(id=pk)
    form = TermNewForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'lms/term/term-edit.html', context)