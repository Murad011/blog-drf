from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from post.api.permissions import IsOwner
from post.api.serializers import PostSerializers, PostUpdateCreateSerializer
from post.models import Post
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView,CreateAPIView, RetrieveUpdateAPIView
from post.api.pagination import PostPagination

class PostListAPIView(ListAPIView):
    serializer_class = PostSerializers
    filter_backends = [SearchFilter]
    search_fields = ['title','content']
    pagination_class = PostPagination


    def get_queryset(self):
        queryset = Post.objects.filter(draft=False)
        return  queryset



class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'
    permission_classes = [IsOwner]

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = PostUpdateCreateSerializer
    serializer_class = PostSerializers
    lookup_field = 'slug'
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by = self.request.user)

class PostCreateAPIView(CreateAPIView, ListModelMixin):
    queryset = PostUpdateCreateSerializer
    serializer_class = PostSerializers
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)




