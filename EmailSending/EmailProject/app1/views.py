from django.shortcuts import render
from .forms import UserForm

from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def signup_view(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            print(email)

            subject = 'Best wishes for your special occasion'
            message = f'Hi {email}, WISH YOU HAPPY BIRTHDAY...!!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
    template_name = 'app1/signup.html'
    context = {'form': form}
    return render(request, template_name, context)
