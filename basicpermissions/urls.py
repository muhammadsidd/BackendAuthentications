from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import NoteViewSet

router = SimpleRouter()
router.register('basicpermissions', NoteViewSet, basename = "basicpermissions")
urlpatterns = router.urls