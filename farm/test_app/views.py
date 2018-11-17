from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseServerError
from django.template import RequestContext, loader, Context
from .protocol_processing import AP3_2
from hikvisionapi import Client
import time
from django.views.decorators import gzip
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from palm.models import Gcg, Anode
from .serializers import GcgSerializer, UserSerializer, AnodeSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

def test_request(request):
    user = request.user
    test_gcg = None
    if user.testgcg_set.exists():
        test_gcg = user.testgcg_set.all()[0]
    return render(request, 'test_app/test_request.html', {
        'user' : user,
        'test_gcg' : test_gcg,
    })
def test_post(request):

    choice = request.POST.get('choice', '')

    return render(request, 'test_app/test_post.html', {
        'value' : choice,
        })
def test_get(request):
    value = request.GET.get('house', '')
    return render(request, 'test_app/test_get.html', {
        'value' : value,
    })
def test_protocol(request):
    ap3 = AP3_2('0x0101010101010101010111010120102013123514532454235234234')
    return HttpResponse(ap3.version)
def test_dict(request):
    dict = {
        '1node_id' : {
            'id' : 1,
            'serial':2,
        },
        '2node_id' : {
            'id' : 2,
            'serial' : 3,
        },
    }
    return render(request, 'test_app/test_dict.html', dict)
# Create your views here.
def index1(request):
    return render(request, 'test_app/index.php')
def index2(request):
    return render(request, 'test_app/index.html')
def index3(request):
    return render(request, 'test_app/index.html')

'''class GcgListAPIView(APIView):
    def get(self, request):
        qs = Gcg.objects.all()
        serializer = GcgSerializer(qs, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = GcgSerializer(data = request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            #return Response(serializer.data, status = 201) - new 지정
        return Response(serializer.errors, status=400)'''
# 수정 삭제 불러오기 를 구현한 클래스 기반의 API view
'''class PostDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        '''
'''@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        serializer = GcgSerializer(Gcg.objects.all(), many=True)
        return Response(serializer.data)
    else:
        serializer = GcgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
from django.shortcuts import get_object_or_404
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    post = get_object_or_404(Gcg, pk=pk)

    if request.method == 'GET':
        serializer = GcgSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GcgSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
'''class GcgListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Gcg.objects.all()
    serializer_class = GcgSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
'''
'''class GcgDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Gcg.objects.all()
    serializer_class = GcgSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
'''# CBV는 중복되는 코드가 존재할때 상속을 위해 사용
class GcgViewSet(viewsets.ModelViewSet):
    queryset = Gcg.objects.all()
    serializer_class = GcgSerializer

    @action(detail=False)  # 목록 단위로 적용할 API이기에, list_route 장식자 사용
    def public_list(self, request, format=None):
        qs = self.queryset.all()  # Post모델에 is_public 필드가 있을 경우
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail = True, methods=['patch'])  # Record 단위로 적용할 API이기에, detail_route 장식자 사용 이때 put은 모든 필드의 수정 patch는 부분수정이 가능
    def set_public(self, request, pk, format=None):
        instance = self.get_object()
        instance.is_public = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    #허나 이코드는 딱히 필요없음 결국 이러한 장식자를 사용한것은 디테일의 영역에서 api를 출력하느냐 리스트의 영역에서 api를 출력하느냐에 따라 default 의 값을 다르게 주어 api를 가공할수있음을 의미한다.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    #search_field = ['id'] 이와같은 경우는 get이자로 serarch가 전달되게 된다 이 api를 호출할때 인자로 search도 같이전달해주면 그에 해당하는 필터링된 json응답을 줄수있을듯
class AnodePageNumberPagination(PageNumberPagination):
    page_size = 20
class AnodeViewSet(viewsets.ModelViewSet):
    queryset = Anode.objects.all()
    serializer_class = AnodeSerializer
    pagination_class = AnodePageNumberPagination

# 이는 나중에 일지작성같은데에서는 20개씩의 데이터를 보내주고 데이터 표현의 페이지에서는 100개의 데이터를 보여주는 부분지정이 필요할듯함
'''class GcgListAPIView(generics.ListAPIView):
    queryset = Gcg.objects.all()
    serializer_class = GcgSerializer
    def get_queryset(self):
        qs = super().get_queryset() # 위의 queryset을 받아온다
        qs = qs.filter(id = 1)  # 직절히 필터링
        return qs
'''
# FBV는 좀더 직관적임 코드가 필요할때 사용 ( 특히 특별한 작업을 하는 view에서 사용 - protocol processing 과 같은)
# API로 요청받았을때 이를 어떻게 처리해야할지 각각 정해두는것이 좋겠네
# 상당히 재밌는 기술이다.
