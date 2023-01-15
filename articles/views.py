from rest_framework.views import APIView
from .serializers import ArticleSerializer
from rest_framework import permissions, status
from .models import Articles
from rest_framework.response import Response



class ArticlesView(APIView):

    serializer_class = ArticleSerializer
    #permission_classes = [permissions.IsAdminUser]

    def get(self,request):
        queryset = Articles.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)