from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns =[
    path('', views.home, name='home'),
    path('main/', views.view_main, name='main'),
    path('search/', views.view_search, name='search'),
    path('write/', views.upload_recipes, name='upload_recipes'),
    path('search/filter/',views.view_filter, name='view_filter'),
    path('search/searching/',views.searching, name='searching'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)