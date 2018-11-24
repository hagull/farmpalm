from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer
from .models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    # 이부분에서 이 리스트를 불러오기 위해선 토큰인증을 해야함을 표현
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    # 이때 모든요청에서 인증헤더에 header = {"Authorizati
    # on: Token 323bf98cf3b6db8168cccc8ed02f9a1150859d2d" message="hello_world"}의 형식으로 보내주어야 한다.
'''res = requests.get(HOST + 'api/post', headers=headers)
res.raise_for_status()
print(res.json())'''
# 이는 리스트를 요청할때
'''
data = {message : ????}
res = requests.post(host+~~ , data = data, header=header)
이는 리스트를 만들때
'''
# Create your views here.
