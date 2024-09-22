from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from drfecommerce.authentication import views as auth
from drfecommerce.cart import views as cart
from drfecommerce.product import views as product
from drfecommerce.wishlist import views as wishlist

router = DefaultRouter()
router.register(r"category", product.CategoryViewSet)
router.register(r"brand", product.BrandViewSet)
router.register(r"product", product.ProductViewSet)
router.register(r"product-line", product.ProductLineViewSet)
router.register(r"product-image", product.ProductImageViewSet)
router.register(r"attribute", product.AttributeViewSet)
router.register(r"attribute-value", product.AttributeValueViewSet)

router.register(r"cart", cart.CartViewSet, basename="cart")
router.register(r"user", auth.UserViewSet)

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
