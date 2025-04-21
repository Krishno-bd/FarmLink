from django.shortcuts import render, redirect
from .forms import ConsultationRequestForm
from django.contrib.auth.decorators import login_required

CONSULTANTS = [
    ('Dr. Md. Mohi Uddin Ahmad', 'Horticulture Specialist'),
    ('Dr. Nowsher Ali Sarder', 'Crop Science Expert'),
    ('Dr. Md. Mizanur Rahman', 'Agrometeorology Consultant'),
    ('Dr. Nabansu Chattopadhyay', 'Agrometeorology Consultant'),
    ('Shamim Hasan', 'Agritech Specialist'),
    ('Mostanser Billah', 'Agricultural Engineer'),
]

@login_required
def consultation_request_view(request):
    if request.method == 'POST':
        form = ConsultationRequestForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.user = request.user
            consultation.save()
            return redirect('consultation:success')
    else:
        form = ConsultationRequestForm()

    return render(request, 'consultation/request_form.html', {'form': form})

@login_required
def consultation_success_view(request):
    return render(request, 'consultation/success.html') 