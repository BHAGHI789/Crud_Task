from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path("",views.create_and_update_profile,name="create_and_update_profile"),
    path("list",views.List_Profile,name="List_Profile")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)