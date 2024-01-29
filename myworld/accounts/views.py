from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages

def send_login_email(request):
    email = request.POST['email']
    print(type(send_mail))
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')