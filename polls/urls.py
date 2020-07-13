from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:fraga_id>/', views.detail, name='detail'),
    path('<int:fraga_id>/results/', views.results, name='results'),
    path('<int:fraga_id>/rosta/', views.results, name='rosta')
]