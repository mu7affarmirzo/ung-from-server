from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/news/', include('news.urls', 'news_api')),
    path('api/tenders/', include('tenders.urls', 'tenders_api')),
    path('api/documents/', include('ungfiles.urls', 'documents_api')),
    path('api/menu/', include('pagenavbar.urls', 'menu_api')),
    path('i18n/', include('django.conf.urls.i18n')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    # path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('news.urls')),
    path('tenders/', include('tenders.urls')),
    path('documents/', include('ungfiles.urls')),
    path('menu/', include('pagenavbar.urls')),

)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)