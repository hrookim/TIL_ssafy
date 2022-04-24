from rest_framework import serializers
from .models import Article, Comment


# GET: R 전체 목록 
# POST: C 
class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title', )


"""------댓글과 관련된 serializer------"""
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', )
"""-------------------------------------"""

# comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

# GET: R detail
# PUT: U
# DELETE: D
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    # article.comment_set.count()에서 manager + API + 괄호 없애서 작성하는 형태!
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


