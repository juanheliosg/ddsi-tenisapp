from rest_framework import routers

from .views import AsignadoSet

router = routers.SimpleRouter()
router.register('horarios', AsignadoSet)

urlpatterns = router.urls
