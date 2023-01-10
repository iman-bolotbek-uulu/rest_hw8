from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Tweet, Comment
from .serializers import TweetSerializer, StatusTweetSerializer, CommentSerializer, StatusCommentSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    @action(methods=['POST'], detail=True)
    def leave_status(self, request, pk=None):
        serializer = StatusTweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                tweet=self.get_object(),
                profile=request.user.profile
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    @action(methods=['POST'], detail=True)
    def leave_status(self, request, pk=None):
        serializer = StatusCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                comment=self.get_object(),
                profile=request.user.profile
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


