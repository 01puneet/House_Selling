
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('Pages.urls')),
    path('listings/', include('Listings.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('Accounts.urls')),
    path('contacts/', include('Contacts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
