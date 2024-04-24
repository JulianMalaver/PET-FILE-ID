from django.shortcuts import render
from .models import Mascota

def formulario_mascota(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        color = request.POST.get('color')
        sexo = request.POST.get('sexo')
        especie = request.POST.get('especie')
        propietario = request.POST.get('propietario')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')

        mascota = Mascota.objects.create(
            nombre=nombre,
            color=color,
            sexo=sexo,
            especie=especie,
            propietario=propietario,
            fecha_nacimiento=fecha_nacimiento
        )

        return render(request, 'formulario_exitoso.html', {'mascota': mascota})
    else:
        return render(request, 'formulario_mascota.html')
