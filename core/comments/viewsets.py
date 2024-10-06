from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import status
from core.abstract.viewsets import AbstractViewSet
from core.comments.models import Comment
from core.comments.serializers import CommentSerializer
from core.auth.permisssions import UserPermission


class CommentViewSet(AbstractViewSet):
    http_method_names = (
        'post',
        'get',
        'put', 
        'delete'
    )
    permission_classes = (UserPermission, )
    serializer_class = CommentSerializer
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Comment.objects.all()
        
        post_pk = self.kwargs['post_pk']
        if post_pk is None:
            return Http404
        return Comment.objects.filter(post__public_id=post_pk)
    
    def get_object(self):
        obj = Comment.objects.get_object_by_public_id(
            self.kwargs['pk']
        )
        self.check_object_permissions(self.request, obj)
        return obj
    
    
    
    