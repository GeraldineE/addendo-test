from rest_framework.viewsets import ModelViewSet
from .models import Organization, Consultant
from .serializers import OrganizationSerializer, ConsultantSerializer


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ConsultantViewSet(ModelViewSet):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
