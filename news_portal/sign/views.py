from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from news.models import Author

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    Author.objects.create (user=user)
    return redirect('/')

# def send_notifications(username, email):
#     html_content = render_to_string(
#         'successful_author_created.html',
#         {
#             'text': username,
            
#         }

#     )

#     msg = EmailMultiAlternatives(
#         subject= email,
#         body='',
#         from_email= settings.DEFAULT_FROM_EMAIL,
#         to = username
#         )
        
