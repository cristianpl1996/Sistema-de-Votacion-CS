from rest_framework import routers
from .viewsets import *

router = routers.SimpleRouter()
router.register('votante', VotanteViewSet)
router.register('eleccion', EleccionViewSet)
router.register('resultado', ResultadoViewSet)
router.register('candidato', CandidatoViewSet)
router.register('partido-politico', PartidoPoliticoViewSet)
urlpatterns = router.urls