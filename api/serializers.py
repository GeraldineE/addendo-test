from rest_framework.serializers import ModelSerializer
from .models import Organization, Consultant


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class ConsultantSerializer(ModelSerializer):
    class Meta:
        model = Consultant
        fields = "__all__"

