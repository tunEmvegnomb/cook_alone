from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns =[
    path('', views.home, name='home'),
    path('search/', views.view_search, name='search'),
    path('write/', views.upload_recipes, name='upload_recipes'),
    path('search/filter/',views.view_filter, name='view_filter'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)