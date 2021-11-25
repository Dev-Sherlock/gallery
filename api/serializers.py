from rest_framework import serializers
from .models import Image
import absoluteuri


class ImageBasicSerializer(serializers.ModelSerializer):
    default = "http://127.0.0.1:5000/api/media/"

    image_200_url = serializers.SerializerMethodField()
    def get_image_200_url(self, Image):
        link = absoluteuri.build_absolute_uri('media/' + str(Image.image_200))
        if link != "http://127.0.0.1:5000/api/media/":
            return link

    class Meta:
        model = Image
        fields = ('__all__')

    def create(self, validated_data):
        return Image.objects.create(**validated_data)




class ImagePremiumSerializer(serializers.ModelSerializer):
    default = "http://127.0.0.1:5000/api/media/"

    image_200_url = serializers.SerializerMethodField()
    def get_image_200_url(self, Image):
        link = absoluteuri.build_absolute_uri('media/' + str(Image.image_200))
        if link != "http://127.0.0.1:5000/api/media/":
            return link

    image_400_url = serializers.SerializerMethodField()
    def get_image_400_url(self, Image):
        link = absoluteuri.build_absolute_uri('media/' + str(Image.image_400))
        if link != "http://127.0.0.1:5000/api/media/":
            return link

    class Meta:
        model = Image
        fields = ('__all__')


    def create(self, validated_data):
        return Image.objects.create(**validated_data)




class ImageEnterpriseSerializer(serializers.ModelSerializer):
    default = "http://127.0.0.1:5000/api/media/"

    image_200_url = serializers.SerializerMethodField()
    def get_image_200_url(self, Image):
        link = absoluteuri.build_absolute_uri('media/' + str(Image.image_200))
        if link != "http://127.0.0.1:5000/api/media/":
            return link


    image_400_url = serializers.SerializerMethodField()
    def get_image_400_url(self, Image):
        link = absoluteuri.build_absolute_uri('media/' + str(Image.image_400))
        if link != "http://127.0.0.1:5000/api/media/":
            return link


    image_original_url = serializers.SerializerMethodField()
    def get_image_original_url(self, Image):
        link = absoluteuri.build_absolute_uri('media/' + str(Image.image_original))
        if link != "http://127.0.0.1:5000/api/media/":
            return link


    class Meta:
        model = Image
        fields = ('__all__')


    def create(self, validated_data):
        return Image.objects.create(**validated_data)

