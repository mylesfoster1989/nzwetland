from rest_framework import routers
from .api import SiteViewSet, HabitatViewSet, LanduseViewSet, SponsorViewSet, AnimalViewSet, SitehabitatlanduseViewSet, SitehabitatViewSet, SurveyViewSet, ObservationViewSet

router = routers.DefaultRouter()
router.register('api/site', SiteViewSet,'site')
router.register('api/habitat', HabitatViewSet,'habitat')
router.register('api/landuse', LanduseViewSet,'landuse')
router.register('api/sitehabitatlanduse', SitehabitatlanduseViewSet,'sitehabitatlanduse')
router.register('api/Sponsor',SponsorViewSet ,'Sponsor')
router.register('api/Animal', AnimalViewSet,'Animal')
router.register('api/Sitehabitat', SitehabitatViewSet,'Sitehabitat')
router.register('api/Survey', SurveyViewSet,'Survey')
router.register('api/Observation', ObservationViewSet,'Observation')

urlpatterns = router.urls
