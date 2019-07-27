from django.http import HttpResponse
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import exceptions


class UserViewSet(mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class TestView(View):
    """
    基于反射实现
    取消csrf认证

    FBV：function base view
    CBV：class base view

    基于中间件的process_view 的
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        print('start' * 300)
        a = super().dispatch(request, *args, **kwargs)
        print('end')
        return a

    def get(self, request, *args, **kwargs):
        return HttpResponse('GET')

    def post(self, request, *args, **kwargs):
        return HttpResponse('GET')


class Authentication:
    def authenticate(self, request):
        # from collections import namedtuple
        #
        # a = namedtuple('User', ['is_authenticated', 'name'])
        """
        Authenticate the request and return a two-tuple of (user, token).
        """
        token = request._request.GET.get('token')
        if token:
            # return a(is_authenticated=True, name='a'), token
            return 'a',token
        raise exceptions.AuthenticationFailed('认证失败')

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        pass


class IndexView(APIView):
    """
    """
    authentication_classes = [Authentication, ]
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return HttpResponse('GET')

    def post(self, request, *args, **kwargs):
        return HttpResponse('GET')


class IndexViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    基于反射实现
    取消csrf认证
    """
    """
       Creates user accounts
       """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
