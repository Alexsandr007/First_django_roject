from django.core.mail import send_mail

def send(user_email,massage):

    send_mail(
        user_email, # main text
        massage, # text
        user_email, # from which mail(с какой почты)
        ['alexandrzambzhitskiy@gmail.com', ],#  which mail(на какую почту)
        fail_silently=False
    )

#celery -A mysite worker -l INFO     -----для запуска celery