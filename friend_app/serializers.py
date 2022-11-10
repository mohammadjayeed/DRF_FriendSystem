from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id','description']

    def create(self, validated_data):
        user_id = self.context['user_id']
        return Post.objects.create(user_id=user_id,**validated_data)



    

    
            

        
    


# class MakePostOwnProfileDataSerializer(serializers.ModelSerializer):

#     class Meta:

