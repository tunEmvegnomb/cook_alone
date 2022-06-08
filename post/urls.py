from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns =[
    path('', views.home, name='home'),
    path('list/', views.view_list, name='list'),
    path('search/', views.view_list, name='search'),
    path('upload/', views.upload_recipes, name='upload_recipes'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)