from nzwetlands.models import Site, Habitat, Landuse, Sponsor, Animal, SiteHabitat, Survey, Observation, \
    Sitehabitatlanduse
from rest_framework import viewsets, permissions
from .serializers import SiteSerializer, HabitatSerializer, LanduseSerializer, SitehabitatlanduseSerializer, \
    SponsorSerializer, AnimalSerializer, SithabitatlanduseSerializer, SiteHabitatSerializer, SurveySerializer, \
    ObservationSerializer


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SiteSerializer


class HabitatViewSet(viewsets.ModelViewSet):
    queryset = Habitat.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HabitatSerializer


class LanduseViewSet(viewsets.ModelViewSet):
    queryset = Landuse.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LanduseSerializer


class SitehabitatlanduseViewSet(viewsets.ModelViewSet):
    queryset = Sitehabitatlanduse.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SitehabitatlanduseSerializer


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SponsorSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnimalSerializer


class SitehabitatlanduseViewSet(viewsets.ModelViewSet):
    queryset = Sitehabitatlanduse.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SithabitatlanduseSerializer


class SitehabitatViewSet(viewsets.ModelViewSet):
    queryset = SiteHabitat.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SiteHabitatSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SurveySerializer


class ObservationViewSet(viewsets.ModelViewSet):
    queryset = Observation.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ObservationSerializer
