from django.urls import path, reverse_lazy
from meds.views import AtcListView, atc_detail, DrugListView, ing_detail, drug_detail, search_index, FavoriteDrugsView, IngListView
from . import views



app_name='meds'

urlpatterns = [

    path('', search_index, name='search-index'),
    path('drug/<int:pk>/', drug_detail, name='drug-detail'),
    path('ing/<int:pk>/', ing_detail, name='ing-detail'),
    path('atc/<int:pk>/', atc_detail, name='atc-detail'),

# urls to the user's favorites list and the favorite/unfavorite toggle functions
    path('favorites/', FavoriteDrugsView.as_view(), name='favorite-drugs'),
    path('drug/<int:pk>/favorite',
    views.AddFavoriteView.as_view(), name='med_favorite'),
    path('drug/<int:pk>/unfavorite',
    views.DeleteFavoriteView.as_view(), name='med_unfavorite'),

# List views that are not to be seen by user and are just for admins/staff
    path('drug/', DrugListView.as_view(), name='index'),
    path('atc/', views.AtcListView.as_view(), name='atc-list'),
    path('ing/', views.IngListView.as_view(), name='ing-list'),

]
