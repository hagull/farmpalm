from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from palm.models import Gcg, Anode
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

class GcgSerializer(ModelSerializer):
    class Meta:
        model = Gcg
        fields = '__all__'
class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
class AnodeSerializer(ModelSerializer):
    class Meta:
        model = Anode
        fields = '__all__'

"""class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)

    def validate_title(self, value):
        if 'django' not in value:
            raise ValidationError('제목에 필히 django가 포함되어야합니다.')
        return value"""
# 위의 코드는 serializer 에서 유효성 검사함수를 지정하는것이다. 이때 반환되는 필드는 non_field_error의 사전인자가 출력된다.
"""class CreateModelMixin(object):
    def create(self, request, *args, **kwargs):              # CREATE 요청이 들어오면,
        serializer = self.get_serializer(data=request.data)  # Serializer 인스턴스를 만들고
        serializer.is_valid(raise_exception=True)            # 유효성 검사를 수행합니다. 실패하면 예외발생 !!!
        self.perform_create(serializer)                      # DB로의 저장을 수행합니다.
        headers = self.get_success_headers(serializer.data)  # 필요한 헤더를 뽑고
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)  # 응답을 합니다.

    def perform_create(self, serializer):                    # CREATE 커스텀은 이 함수를 재정의하세요.
        serializer.save()"""
# 이때 이 perform_create는 재정의 하여서 ip주소를 자동으로 받는것이 가능 - 이는 유용할듯
"""def perform_create(self, serializer):
    # ip 필드가 있다면 ? 여기서 이 perform_create 재정의를 통해서 이미 인증된 유저에 대해서도 다룰수있다.
    serializer.save(author=self.request.user,
                    ip=self.request.META['REMOTE_ADDR'])"""
# 이런식으로 재정의 하여서 유저의 ip주소를 받는다 즉 creat시에 추가로 필드를 설정할때 씀 여기서는 ip주소를 추가로 받음
