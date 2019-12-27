import inspect

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from web_admin import models


class ModelInit(APIView):
    def get(self, request, *args, **kwargs):
        abcd = {}
        for name, obj in inspect.getmembers(models):
            if name in ('CommonModel', 'PRODUCT_ONLINE_STATUS', 'DELETE_STATUS', 'DISSENT_RECOMMEND_WAY', 'models'):
                continue
            if name.startswith('_'):
                continue

            fields = []
            if inspect.isclass(obj) and '_meta' in obj.__dict__:
                for i in obj._meta.fields:
                    fields.append("'{}'".format(i.name))

            abc = """
class {name}Serializer(BaseModelSerialize):
    class Meta:
        model = {name}
        fields = ({fields})
        read_only_fields = ('id', 'update_datetime',)


class {name}ViewSet(BaseViewSet):

    queryset = {name}.objects.all()
    serializer_class = {name}Serializer""".format(name=name, fields=",".join(fields))
            print(abc)
            abcd[name] = '{name}ViewSet'.format(name=name)
            # print('{} - {}'.format(name, obj))

        for a, b in abcd.items():
            print("router.register(r'{}', {})".format(a, b))

        return Response({'status': abc}, status=status.HTTP_200_OK)
