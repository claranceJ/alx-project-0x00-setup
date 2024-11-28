from DjangoDB.urls import urlpatterns
from dbapp import views
urlpatterns = [
    path('', views.index, name='index'),


]