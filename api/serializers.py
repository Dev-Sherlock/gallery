from rest_framework import serializers
from .models import Image
import absoluteuri


class ImageSerializer(serializers.ModelSerializer):
    default = "http://127.0.0.1:5000/api/media/"

    account_type = serializers.SerializerMethodField()

    def get_account_type(self, obj):
        account_type = self.context.get("account_type")
        return account_type

    if str(account_type) == "Basic":
        image_200_url = serializers.SerializerMethodField()

        def get_image_200_url(self, Image):
            link = absoluteuri.build_absolute_uri('media/' + str(Image.image_200))
            if link != "http://127.0.0.1:5000/api/media/":
                return link

        class Meta:
            model = Image
            exclude = ('image_original','image_200','image_400')


    elif str(account_type) == "Premium":
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
            exclude = ('image_original','image_200','image_400')


    else:

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
            exclude = ('image_original','image_200','image_400')

    def create(self, validated_data):
        return Image.objects.create(**validated_data)

