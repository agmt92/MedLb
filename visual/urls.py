from django.urls import path
from . import views


app_name='visual'

urlpatterns = [
    path('', views.drug_visualization, name='drug-visualization'),
    path('guide/', views.visualization_guide, name='visualization-guide'),
]
