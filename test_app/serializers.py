from rest_framework import serializers

from test_app.models import SampleModel


class SampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleModel
        fields = '__all__'
