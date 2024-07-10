from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Event
from .forms import EventForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            #event.created_by = request.user
            event.organizer = request.user  # Definindo o organizador
            event.created_by = request.user  # Definindo o criador
            event.save()
            #return redirect('event_list')
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    #return render(request, 'event_form.html', {'form': form})
    return render(request, 'event_create.html', {'form': form})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})

@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if event.created_by != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'event_edit.html', {'form': form, 'event': event})

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if event.created_by != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'event_confirm_delete.html', {'event': event})


