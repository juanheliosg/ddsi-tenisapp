from rest_framework import routers

from .views import CompraSet, AsignadoSet, PartidoSet

router = routers.SimpleRouter()
router.register('horarios', AsignadoSet)
router.register('partidos', PartidoSet)
router.register('compra', CompraSet)

urlpatterns = router.urls
