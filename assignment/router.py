from api_requests.viewsets import ProfileViewset
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('v1/user',ProfileViewset)