from django.contrib import admin
from django.urls import path, include

from . import views

handler404 = "oc_lettings_site.views.view_error_404"
handler500 = "oc_lettings_site.views.view_error_500"

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include("lettings.urls")),
    path('profiles/', include("profiles.urls")),
    path('admin/', admin.site.urls),
]
