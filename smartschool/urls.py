
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include ( 'formation.urls')),
    path('api/', include ( 'account.urls')),
    path('api/', include ( 'order.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'utils.error_view.handler404'
handler500 = 'utils.error_view.handler500'
