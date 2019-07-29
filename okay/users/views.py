from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Student, LearnGroup, Course, PricePolicy, DegreeCourse
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
            return 'a', token
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


# class StudentView(APIView):
#     """
#     // 20190728162948
#     // http://0.0.0.0:8000/students/
#
#     {
#       "data": [
#         {
#           "name": "lishulong",
#           "age": 12,
#           "learn_group": 1,
#           "teachers": 1
#         }
#       ]
#     }
#     """
#     def get(self, request):
#         a = Student.objects.all().values('name', 'age', 'learn_group', 'teachers')
#         return JsonResponse(dict(data=list(a)))

from rest_framework import serializers


# class StudentSerializers(serializers.Serializer):
#     name = serializers.CharField()
#     age = serializers.IntegerField()
#     gender_ = serializers.CharField(source="gender")
#     gender_1 = serializers.CharField(source="get_gender_display")
#
#     learn_group = serializers.CharField()
#     learn_group_1 = serializers.CharField(source="learn_group.title")
#
#     teachers = serializers.CharField(source='teachers.all')
#
#     teachers_ = serializers.SerializerMethodField()
#
#     def get_teachers_(self, row):
#         return {i.id: i.name for i in row.teachers.all()}
#
#     def create(self, validated_data):
#         pass
#
#     def update(self, instance, validated_data):
#         pass
#
#
# class StudentView(APIView):
#     def get(self, request):
#         a = Student.objects.all()
#         s = StudentSerializers(instance=a, many=True)
#         return JsonResponse(dict(data=s.data))


class StudentSerializer(serializers.ModelSerializer):
    teachers_ = serializers.SerializerMethodField()

    group_3 = serializers.HyperlinkedIdentityField(view_name='learn_group', lookup_field="learn_group_id",
                                                   lookup_url_kwarg="pk")

    def get_teachers_(self, row):
        return {i.id: i.name for i in row.teachers.all()}

    class Meta:
        model = Student
        # fields = ('name', 'age')
        depth = 2
        fields = "__all__"
        extra_fields = ('teachers', 'name1', 'group_3')

        extra_kargs = {'name1': {
            'source': "learn_group.title"
        }}


class StudentView(APIView):
    def get(self, request, *args, **kwargs):
        data = StudentSerializer(instance=Student.objects.all(), many=True,
                                 context={'request': request}).data
        return JsonResponse(dict(data=data))


class LearnGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearnGroup
        fields = "__all__"


class TitleValidator:
    def __init__(self, v):
        self.value = v

    def __call__(self, value):
        if not value.startswith(self.value):
            message = f'This field must starts with: {self.value}'
            raise serializers.ValidationError(message)

    def set_context(self, serializer_field):
        pass


class LearnGroupSerializer1(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return LearnGroup.objects.create(**validated_data)

    title = serializers.CharField(error_messages={"required": "标题不能为None"}, validators=[TitleValidator('嘿嘿')])


class LearnGroupView(APIView):
    from rest_framework.parsers import JSONParser, FormParser
    parser_classes = [JSONParser, FormParser]

    def get(self, request, *args, **kwargs):
        data = LearnGroupSerializer(
            instance=LearnGroup.objects.filter(pk=kwargs.get('pk')),
            many=True).data
        return JsonResponse(dict(data=data))

    def post(self, request, *args, **kwargs):
        s = LearnGroupSerializer1(data=request.data)
        if s.is_valid():
            a = s.create(s.validated_data)
            return JsonResponse(data=LearnGroupSerializer1(instance=a, many=False).data)
        else:
            print(s.errors)
            return JsonResponse(data=s.errors)


from rest_framework.serializers import ModelSerializer


class MMModelSerializer(ModelSerializer):
    class Meta:
        model = PricePolicy
        fields = '__all__'
        depth = 1


class CourseView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Course.objects.all()

    serializer_class = MMModelSerializer

    def list(self, request, *args, **kwargs):
        Course.objects.create(**{
            'title': "math¬"
        })
        DegreeCourse.objects.create(**{
            'title': "语文"
        })

        c = Course.objects.filter().first()
        d = DegreeCourse.objects.all().first()
        PricePolicy.objects.create(price=1.2, periods=1, content_object=c)
        PricePolicy.objects.create(price=1.3, periods=2, content_object=c)
        PricePolicy.objects.create(price=1.4, periods=3, content_object=c)
        PricePolicy.objects.create(price=11.4, periods=13, content_object=d)
        PricePolicy.objects.create(price=12.4, periods=23, content_object=d)
        PricePolicy.objects.create(price=13.4, periods=33, content_object=d)

        pps = c.policy_list.all()

        s = MMModelSerializer(instance=pps, many=True)

        print(pps)
        return Response(s.data)
