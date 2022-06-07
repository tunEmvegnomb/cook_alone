from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns =[
    path('', views.home, name='home'),
    path('list/', views.view_list, name='list'),
    path('upload/', views.upload_recipes, name='upload_recipes'),
]

if settings.DEBUG:#<-세팅이 개발자모드일때,
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #<-url에 미디어 루트도 추가한다