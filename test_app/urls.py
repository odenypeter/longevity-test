from rest_framework import routers
from views import SampleModelViewSet

router = routers.SimpleRouter()
router.register(r'sample-model', SampleModelViewSet, basename='sample-model')
