from django.urls import include, path
from rest_framework.routers import SimpleRouter

from cats.views import CatList, CatDetail, CatViewSet

router = SimpleRouter()
router.register('cats', CatViewSet, basename='cats')

urlpatterns = [
   path('', include(router.urls)),
]
