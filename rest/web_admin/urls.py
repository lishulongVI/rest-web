from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from init_model_view import ModelInit
from web_admin.views import ProductViewSet, ProductStageViewSet, ProductStageSpeechSkillViewSet

router = routers.DefaultRouter()
router.register(r'production', ProductViewSet)
router.register(r'production_stage', ProductStageViewSet)
router.register(r'production_stage_speech_skill', ProductStageSpeechSkillViewSet)
urlpatterns = [
    url('', include((router.urls, 'production'))),
    url('init', ModelInit.as_view()),
]
