from rest_framework.routers import DefaultRouter
from .views import FaqAilabViewSet

router = DefaultRouter()
router.register(r'faq-ailab', FaqAilabViewSet, basename='faq-ailab')

urlpatterns = router.urls
