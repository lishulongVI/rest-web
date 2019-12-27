# Create your views here.

from base_views import BaseModelSerialize, BaseViewSet
from web_admin.models import (
    Product, ProductStage, ProductStageSpeechSkill,
    Dissent, DissentSpeechSkill, ConversationNote,
    SpeechSkillTagGroup)


class ProductSerializer(BaseModelSerialize):
    class Meta:
        model = Product
        fields = ('id', 'product_name', 'product_desc', 'online_state', 'update_datetime')
        read_only_fields = ('id', 'update_datetime')


class ProductViewSet(BaseViewSet):
    """
    产品管理
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductStageSerializer(BaseModelSerialize):
    class Meta:
        model = ProductStage
        fields = ('id', 'product_id', 'stage_name', 'stage_order', 'update_datetime', 'deleted')
        read_only_fields = ('id', 'update_datetime',)


class ProductStageViewSet(BaseViewSet):
    """
    产品阶段管理
    """
    queryset = ProductStage.objects.all()
    serializer_class = ProductStageSerializer


class ProductStageSpeechSkillSerializer(BaseModelSerialize):
    class Meta:
        model = ProductStageSpeechSkill
        fields = ('id', 'product_stage_id', 'speech_title', 'speech_desc', 'tag_values', 'update_datetime', 'deleted')
        read_only_fields = ('id', 'update_datetime',)


class ProductStageSpeechSkillViewSet(BaseViewSet):
    """
    产品阶段话术管理
    """
    queryset = ProductStageSpeechSkill.objects.all()
    serializer_class = ProductStageSpeechSkillSerializer

    def update(self, request, *args, **kwargs):
        pass


class ConversationNoteSerializer(BaseModelSerialize):
    class Meta:
        model = ConversationNote
        fields = ('id', 'deleted', 'create_datetime', 'update_datetime', 'conversation_id', 'text_content')
        read_only_fields = ('id', 'update_datetime',)


class ConversationNoteViewSet(BaseViewSet):
    queryset = ConversationNote.objects.all()
    serializer_class = ConversationNoteSerializer


class DissentSerializer(BaseModelSerialize):
    class Meta:
        model = Dissent
        fields = ('id', 'deleted', 'create_datetime', 'update_datetime', 'dissent_name', 'sequence_matcher_text',
                  'sequence_matcher_ratio', 'text_reg', 'incr_validate_ms', 'decr_validate_ms', 'recommend_way',
                  'speech_num')
        read_only_fields = ('id', 'update_datetime',)


class DissentViewSet(BaseViewSet):
    queryset = Dissent.objects.all()
    serializer_class = DissentSerializer


class DissentSpeechSkillSerializer(BaseModelSerialize):
    class Meta:
        model = DissentSpeechSkill
        fields = (
            'id', 'deleted', 'create_datetime', 'update_datetime', 'dissent_id', 'speech_title', 'speech_desc',
            'hot_value')
        read_only_fields = ('id', 'update_datetime',)


class DissentSpeechSkillViewSet(BaseViewSet):
    queryset = DissentSpeechSkill.objects.all()
    serializer_class = DissentSpeechSkillSerializer


class SpeechSkillTagGroupSerializer(BaseModelSerialize):
    class Meta:
        model = SpeechSkillTagGroup
        fields = ('id', 'deleted', 'create_datetime', 'update_datetime', 'tag_name', 'tag_value')
        read_only_fields = ('id', 'update_datetime',)


class SpeechSkillTagGroupViewSet(BaseViewSet):
    queryset = SpeechSkillTagGroup.objects.all()
    serializer_class = SpeechSkillTagGroupSerializer
