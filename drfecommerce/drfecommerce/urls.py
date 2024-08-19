from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drfecommerce.product import views as product
from drfecommerce.authentication import views as auth
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r"category", product.CategoryViewSet)
router.register(r"brand", product.BrandViewSet)
router.register(r"product", product.ProductViewSet)
router.register(r"product-line", product.ProductLineViewSet)
router.register(r"product-image", product.ProductImageViewSet)
router.register(r"attribute", product.AttributeViewSet)
router.register(r"attribute-value", product.AttributeValueViewSet)

# auth_router = DefaultRouter()
# auth_router.register(r"register", auth.RegisterView.as_view(), name="register")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    # path("auth/", include(auth_router.urls)),
    path("auth/", include("drfecommerce.authentication.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]
