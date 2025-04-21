from django.shortcuts import render
from .data import FERTILIZER_DATA

def fertilizer_calculator(request):
    result = None
    if request.method == 'POST':
        crop = request.POST.get('crop')
        land_size = float(request.POST.get('land_size', 1))
        crop_data = FERTILIZER_DATA.get(crop)

        if crop_data:
            result = {name: amount * land_size for name, amount in crop_data.items()}

    context = {
        'crops': FERTILIZER_DATA.keys(),
        'result': result
    }
    return render(request, 'fertilizer/calculator.html', context)
