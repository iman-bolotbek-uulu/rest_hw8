from rest_framework import serializers

from .models import Tweet, Comment, StatusTweet, StatusComment


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'
        read_only_fields = ['profile', ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['profile', ]


class StatusTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTweet
        fields = '__all__'
        read_only_fields = ['profile', 'tweet']


class StatusCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusComment
        fields = '__all__'
        read_only_fields = ['profile', 'comment']