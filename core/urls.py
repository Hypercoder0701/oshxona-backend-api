from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Oshxona Avtomatlishitirilgan tizim uchun API",
        default_version='v1',
        description="",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from rest_framework.routers import DefaultRouter

from main.views import *

router = DefaultRouter()

router.register('bolimlar', BolimViewSet)
router.register('taomlar', TaomViewSet)
router.register('stollar', StolViewSet)
router.register('buyurtmalar', BuyurtmaViewSet)
router.register('buyurtma-taomlar', BTaomViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),

]
