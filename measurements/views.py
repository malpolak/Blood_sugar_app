from django.shortcuts import render, get_object_or_404, redirect
from measurements.models import Measurement


def measurement_list(request):
    measurements = Measurement.objects.all()
    return render(request, "measurements/measurement_list.html", {"measurements": measurements})

def measurement_detail(request, measurement_id):
    measurement = get_object_or_404(Measurement, pk=measurement_id)
    return render(request, 'measurements/measurement_detail.html', {'measurement': measurement})

def measurement_delete(request, measurement_id):
    if request.method == 'POST':
        if request.POST.get('action') == 'delete':
            measurement = get_object_or_404(Measurement, id=measurement_id)
            measurement.delete()
            return redirect('measurement_list')

        elif request.POST.get('action') == 'back':
            return redirect('measurement_list')

    measurement = get_object_or_404(Measurement, id=measurement_id)
    context = {'measurement': measurement}
    return render(request, 'measurement_delete.html', context)
