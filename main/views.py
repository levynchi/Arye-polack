from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Performance, Track, ContactMessage


def home(request):
    import datetime
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message_text = request.POST.get('message', '').strip()
        if name and email and message_text:
            ContactMessage.objects.create(name=name, email=email, message=message_text)
            return render(request, 'main/home.html', {
                'tracks': Track.objects.all(),
                'upcoming': Performance.objects.filter(date__gte=datetime.date.today()),
                'past': Performance.objects.filter(date__lt=datetime.date.today()),
                'contact_success': True,
            })
    return render(request, 'main/home.html', {
        'tracks': Track.objects.all(),
        'upcoming': Performance.objects.filter(date__gte=__import__('datetime').date.today()),
        'past': Performance.objects.filter(date__lt=__import__('datetime').date.today()),
    })


def about(request):
    return render(request, 'main/about.html')


def music(request):
    tracks = Track.objects.all()
    return render(request, 'main/music.html', {'tracks': tracks})


def performances(request):
    upcoming = Performance.objects.filter(date__gte=__import__('datetime').date.today())
    past = Performance.objects.filter(date__lt=__import__('datetime').date.today())
    return render(request, 'main/performances.html', {'upcoming': upcoming, 'past': past})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message_text = request.POST.get('message', '').strip()
        if name and email and message_text:
            ContactMessage.objects.create(name=name, email=email, message=message_text)
            messages.success(request, 'ההודעה נשלחה בהצלחה! אחזור אליך בהקדם.')
            return redirect('contact')
    return render(request, 'main/contact.html')
