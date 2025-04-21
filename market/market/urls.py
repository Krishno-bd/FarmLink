from django.urls import include, path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),

    path('Account/', include('Account.urls')),

    # products
    path("", include("product.urls")),

    # dashboard urls
    path("dashboard/", include("dashboard.urls")),

    # cart urls
    # path("cart/", include("cart.urls")),
   # path('wishlist/', include('cart.urls')),  # or 'wishlist.urls' if separate app

    # project/urls.py
    # path('wishlist/', include('cart.urls', namespace='cart')),  # Only do this if splitting

    path("cart/", include("cart.urls", namespace='cart')),
    path('feedback/', include('feedback.urls')),
    path('consultation/', include('consultation.urls')),
    path('fertilizer/', include('fertilizer.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)