
from rest_framework import serializers
from posts.models import Article
from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin
# class AuthorUsernameField(serializers.RelatedField):
#     def to_representation(self, value):
#         return value.username

class ArticleSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
 # line6
    class Meta :
        model = Article
        fields="__all__"
        # fields = ("title", "context", "author")
        # exclude=("status")
    # line6 below
    # def get_author (self,obj):
    #     return {
    #         "username":obj.author.username,
    #         "first_name": obj.author.first_name,
    #         "last_name": obj.author.last_name,
    #     }
    #
    # author = serializers.SerializerMethodField("get_author")

    # def validate_title(self,value):
    #     filter_list=["javascript","php","larave"]
    #     for i in filter_list:
    #         for i in value:
    #             raise serializers.ValidationError("dont use bad worlds ! : {}".format(i))


class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = get_user_model()
        fields = ("__all__")





