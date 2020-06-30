from rest_framework import routers
from .viewsets import OrganizationViewSet, ConsultantViewSet

router = routers.DefaultRouter()
router.register("org", OrganizationViewSet)
router.register("consultant", ConsultantViewSet)
