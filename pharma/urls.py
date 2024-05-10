# pharma/urls.py

from django.urls import path
from pharma.views import pharmacy_search, FavoritePharmacyView, AddFavoritePharmacyView, DeleteFavoritePharmacyView
from . import views

app_name='pharma'


urlpatterns = [
    path('', pharmacy_search, name='pharmacy-list'),

    # URL to view the user's favorite pharmacies list (assuming there's a view for this)
    path('favorites/', FavoritePharmacyView.as_view(), name='pharmacy_favorite'),
    path('pharmacy/<int:pk>/favorite', views.AddFavoritePharmacyView.as_view(), name='pharma_favorite'),
    path('pharmacy/<int:pk>/unfavorite', views.DeleteFavoritePharmacyView.as_view(), name='pharma_unfavorite'),
]
