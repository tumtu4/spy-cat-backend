import requests
from rest_framework import serializers
from .models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = "__all__"

    def validate_breed(self, value):
        """
        Validate breed using TheCatAPI
        """
        response = requests.get("https://api.thecatapi.com/v1/breeds")

        if response.status_code != 200:
            raise serializers.ValidationError("Unable to validate breed at this time.")

        breeds = response.json()
        breed_names = [breed["name"].lower() for breed in breeds]

        if value.lower() not in breed_names:
            raise serializers.ValidationError("Invalid breed according to TheCatAPI.")

        return value


class CatSalaryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ["salary"]