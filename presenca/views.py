from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Lista

def presenca(request):
    total = request.session.get('total', 0)

    if request.method == 'POST':
        if 'presenca' in request.POST:
            total += 1
            request.session['total'] = total
        if 'finalizar' in request.POST:
            if total > 0:
                agora = timezone.localtime()  # horário PT-BR
                Lista.objects.create(
                    data=agora.date(),
                    hora=agora.time(),
                    total=total
                )
                request.session['total'] = 0


    return render(request, 'presenca.html', {'total': total})
