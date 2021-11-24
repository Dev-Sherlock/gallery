from .models import *
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import Image


class ImageListView(APIView):
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        images = Image.objects.filter(user__user=user)
        user= UserProfile.objects.get(user=self.request.user)
        if user.type=='Basic':
            serializer = ImageBasicSerializer(images, many=True)
        elif user.type=='Premium':
            serializer = ImagePremiumSerializer(images, many=True)
        else:
            serializer = ImageEnterpriseSerializer(images, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ImageBasicSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(
                user=UserProfile.objects.get(user=request.user.username),
                image_original=request.data.get('image'),
                image_200=request.data.get('image'),
                image_400=request.data.get('image'),
            )
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


