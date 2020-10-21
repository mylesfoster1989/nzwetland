from rest_framework import serializers
from nzwetlands.models import Site, Habitat, Landuse, Sponsor, Animal, SiteHabitat, Survey, Observation, Sitehabitatlanduse


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'


class HabitatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitat
        fields = '__all__'


class LanduseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landuse
        fields = '__all__'


class SitehabitatlanduseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitehabitatlanduse
        fields = '__all__'

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class SithabitatlanduseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitehabitatlanduse
        fields = '__all__'


class SiteHabitatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteHabitat
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'


class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = '__all__'
