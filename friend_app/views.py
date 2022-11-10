from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import *
from .serializers import *

    
class PostViewSet(ModelViewSet):
    
    serializer_class = PostSerializer


    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user.id)

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}
