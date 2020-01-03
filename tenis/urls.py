from rest_framework import routers

from .views import AsignadoSet, PartidoSet

router = routers.SimpleRouter()
router.register('horarios', AsignadoSet)
router.register('partidos', PartidoSet)

urlpatterns = router.urls
