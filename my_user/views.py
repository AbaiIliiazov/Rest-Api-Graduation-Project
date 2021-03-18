from django.contrib.sites.shortcuts import get_current_site
from .models import User
from rest_framework import decorators, response, status
from rest_framework.renderers import JSONRenderer
from .serializers import UserCreateSerializer,UserEditSerializer
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import EmailMultiAlternatives
from rest_framework import generics
from persproj.settings import DEFAULT_FROM_EMAIL
from rest_framework.permissions import IsAuthenticated


@decorators.api_view(['POST','GET'])
@decorators.renderer_classes([JSONRenderer])
def register(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    user.is_active = False
    user.save()
    current_site = get_current_site(request)
    mail_subject = 'Activate your account'
    to_email = user.email
    message = render_to_string('confirmation.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user)
        })
    email = EmailMultiAlternatives(mail_subject, message, from_email=DEFAULT_FROM_EMAIL,to=[to_email])
    email.content_subtype = 'html'
    email.send()
    return response.Response('Email was sent for confirmation', status.HTTP_201_CREATED)

@decorators.api_view(['POST','GET'])
@decorators.renderer_classes([JSONRenderer])

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        refresh = RefreshToken.for_user(user)
        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return response.Response(res)
    else:
        return response.Response('Invalid')

class UserDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = UserEditSerializer
    permission_classes = [IsAuthenticated,]

    def get(self, request, *args, **kwargs):
        serializer=self.serializer_class(request.user)
        print("USER SERIALIZER", serializer)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

