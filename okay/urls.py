from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .users.views import UserViewSet, UserCreateViewSet, TestView, IndexView, StudentView, LearnGroupView, CourseView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)
router.register(r'course', CourseView)
# router.register(r'index', IndexViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('test/', TestView.as_view()),
    path('index/', IndexView.as_view()),
    path('students/', StudentView.as_view()),
    path(r'learn_group/<pk>/', LearnGroupView.as_view(), name='learn_group'),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

]
urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
