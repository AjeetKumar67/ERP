from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Event, Announcement
from .forms import EventForm, AnnouncementForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_notice_board/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_notice_board/event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('event_notice_board:event_list'))
    else:
        form = EventForm()
    return render(request, 'event_notice_board/event_form.html', {'form': form})

def event_update(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('event_notice_board:event_detail', args=[event.id]))
    else:
        form = EventForm(instance=event)
    return render(request, 'event_notice_board/event_form.html', {'form': form})

def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return HttpResponseRedirect(reverse('event_notice_board:event_list'))
    return render(request, 'event_notice_board/event_confirm_delete.html', {'event': event})

def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'event_notice_board/announcement_list.html', {'announcements': announcements})

def announcement_create(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('event_notice_board:announcement_list'))
    else:
        form = AnnouncementForm()
    return render(request, 'event_notice_board/announcement_form.html', {'form': form})

def announcement_update(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('event_notice_board:announcement_list'))
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'event_notice_board/announcement_form.html', {'form': form})

def announcement_delete(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    if request.method == 'POST':
        announcement.delete()
        return HttpResponseRedirect(reverse('event_notice_board:announcement_list'))
    return render(request, 'event_notice_board/announcement_confirm_delete.html', {'announcement': announcement})