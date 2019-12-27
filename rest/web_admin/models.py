from django.db import models

# Create your models here.
from web_admin.constants import DELETE_STATUS, PRODUCT_ONLINE_STATUS, DISSENT_RECOMMEND_WAY


class CommonModel(models.Model):
    id = models.AutoField(primary_key=True)

    deleted = models.IntegerField(verbose_name='是否删除', choices=DELETE_STATUS, default=0)
    create_datetime = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name='创建时间'
    )
    update_datetime = models.DateTimeField(
        auto_now=True,
        null=True,
        verbose_name='修改时间'
    )

    class Meta:
        abstract = True


class Product(CommonModel):
    """
    产品
    """
    product_name = models.CharField(verbose_name='产品名称', max_length=64, blank=True, null=True)
    product_desc = models.CharField(verbose_name='产品描述', max_length=255, blank=True, null=True)
    online_state = models.IntegerField(verbose_name='上线状态', choices=PRODUCT_ONLINE_STATUS, default=1)

    class Meta:
        db_table = 'product'
        verbose_name = '产品'
        verbose_name_plural = '产品管理'

    def __str__(self):
        return repr(self.id)


class ProductStage(CommonModel):
    """
    产品阶段
    """
    product_id = models.IntegerField(verbose_name="产品ID", blank=True, null=True)
    stage_name = models.CharField(verbose_name='阶段名称', max_length=64, blank=True, null=True)
    stage_order = models.IntegerField(verbose_name='产品阶段序列', blank=True, null=True, default=0)

    class Meta:
        db_table = 'product_stage'
        verbose_name = '产品阶段'
        verbose_name_plural = '产品阶段管理'
        indexes = [models.Index(fields=['product_id'], name='idx_product_id')]


class ProductStageSpeechSkill(CommonModel):
    """
    产品阶段话术
    """

    product_stage_id = models.IntegerField(verbose_name="产品阶段ID", blank=True, null=True)
    speech_title = models.CharField(verbose_name='话术标题', max_length=64, blank=True, null=True)
    speech_desc = models.TextField(verbose_name='阶段话术', blank=True, null=True)
    tag_values = models.CharField(verbose_name='话术标签值', max_length=512, blank=True, null=True)

    class Meta:
        db_table = 'product_stage_speech_skill'
        verbose_name_plural = '产品阶段话术管理'
        verbose_name = '产品阶段话术'
        indexes = [models.Index(fields=['product_stage_id'], name='idx_product_stage_id')]


class SpeechSkillTagGroup(CommonModel):
    """
    标签组
    """
    tag_name = models.CharField(verbose_name='标签名称', max_length=64, blank=True, null=True)
    tag_value = models.TextField(verbose_name='标签值', blank=True, null=True)

    class Meta:
        db_table = 'tags'
        verbose_name = '标签组'
        verbose_name_plural = '标签组管理'


class Dissent(CommonModel):
    """
    异议
    """
    dissent_name = models.CharField(verbose_name="异议名称", max_length=64, blank=True, null=True)
    sequence_matcher_text = models.TextField(verbose_name="文本匹配", max_length=512, blank=True, null=True)
    sequence_matcher_ratio = models.FloatField(verbose_name="文本相似度", null=True, blank=True)
    text_reg = models.CharField(verbose_name="正则匹配", max_length=512, null=True, blank=True)
    incr_validate_ms = models.IntegerField(verbose_name='通话持续时间加1规则')
    decr_validate_ms = models.IntegerField(verbose_name='通话持续时间减1规则')
    recommend_way = models.IntegerField(verbose_name='推荐方式', default=1, choices=DISSENT_RECOMMEND_WAY)
    speech_num = models.IntegerField(verbose_name='话术数量', default=0)

    class Meta:
        db_table = 'dissent'
        verbose_name = '异议'


class DissentSpeechSkill(CommonModel):
    """
    异议话术
    """
    dissent_id = models.IntegerField(verbose_name="异议ID", blank=False, null=False)
    speech_title = models.CharField(verbose_name='标题', max_length=512, blank=True, null=True)
    speech_desc = models.TextField(verbose_name='话术', blank=True, null=True)
    hot_value = models.IntegerField(verbose_name='置信度', blank=True, null=True)

    class Meta:
        db_table = 'dissent_speech_skill'
        verbose_name_plural = '异议话术管理'
        verbose_name = '异议话术'
        indexes = [models.Index(fields=['dissent_id'], name='idx_dissent_id')]


class ConversationNote(CommonModel):
    """
    记事本
    """
    conversation_id = models.IntegerField(verbose_name="通话ID")
    text_content = models.TextField(verbose_name="文本内容")

    class Meta:
        db_table = 'conversation_note'
        verbose_name = "记事本"
        indexes = [models.Index(fields=['conversation_id'], name='idx_conversation_id')]

