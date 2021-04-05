from django.urls import path
from app1 import views
app_name="app1"


urlpatterns = [
    path('',views.index,name="page1"),
    path('sample1/',views.hello,name="sample1"),
    path('sam/',views.sample_app1,name="sample2"),
]
