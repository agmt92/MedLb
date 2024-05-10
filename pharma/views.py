from django.views.generic import ListView
from django.db.models import Q
from .models import Pharmain, FavoritePharmacy
from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Case, When, Value, IntegerField


def pharmacy_search(request):
    search_query = request.GET.get('q', '')
    search_field = request.GET.get('field', 'all')  # 'all' is the default search field
    pharmacies = Pharmain.objects.all()
    sort_order = request.GET.get('sort', 'relevance')


    if search_query:
        # Define Q objects for each search field
        search_conditions = {
            'all': Q(phanam__icontains=search_query) |
                   Q(phacistnam__icontains=search_query) |
                   Q(address__addnam__icontains=search_query) |
                   Q(address__casa__casnam__icontains=search_query) |
                   Q(address__casa__mouhafaza__mounam__icontains=search_query),
            'phanam': Q(phanam__icontains=search_query),
            'phacistnam': Q(phacistnam__icontains=search_query),
            'addnam': Q(address__addnam__icontains=search_query),
            'casnam': Q(address__casa__casnam__icontains=search_query),
            'mounam': Q(address__casa__mouhafaza__mounam__icontains=search_query),
        }

        # Apply the selected search condition
        pharmacies = pharmacies.filter(search_conditions.get(search_field, search_conditions['all']))
    else:
        pharmacies = Pharmain.objects.none()  # Return no results if there's no search query

    # Apply sorting
    if sort_order == 'alph_asc':
        pharmacies = pharmacies.order_by('phanam')
    elif sort_order == 'alph_desc':
        pharmacies = pharmacies.order_by('-phanam')
    elif sort_order == 'relevance':
        # Sorting by relevance - exact matches first, then partial matches
        pharmacies = pharmacies.annotate(
            exact_match=Case(
                When(phanam__iexact=search_query, then=Value(1)),
                default=Value(0),
                output_field=IntegerField()
            )
        ).order_by('-exact_match', 'phanam')

    # Pagination setup
    paginator = Paginator(pharmacies, 15)  # Show 15 pharmacies per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Handling favorites
    favorites = []
    if request.user.is_authenticated:
        favorites = list(request.user.favoritepharmacy_set.values_list('pharmacy_id', flat=True))

    context = {
        'page_obj': page_obj,
        'query': search_query,
        'search_field': search_field,  # Include the selected search field in the context
        'favorites': favorites,
        'sort_order': sort_order
    }
    return render(request, 'pharma/pharmacy_list.html', context)


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class FavoritePharmacyView(LoginRequiredMixin, generic.ListView):
    model = Pharmain
    template_name = 'pharma/favorite_pharmacies.html'  # Path to your template
    context_object_name = 'favorite_pharmacies'

    def get_queryset(self):
        # Get the current user's favorites
        user_favorites = FavoritePharmacy.objects.filter(user=self.request.user)
        # Extract the Pharmain ids from user_favorites
        favorite_ids = user_favorites.values_list('pharmacy', flat=True)
        # Filter the Pharmacies that are in the user's favorites
        return Pharmain.objects.filter(id__in=favorite_ids)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add additional context if needed
        return context

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoritePharmacyView(LoginRequiredMixin, View):
    def post(self, request, pk):
        print("Adding Pharmacy to Favorites, PK:", pk)
        t = get_object_or_404(Pharmain, id=pk)
        fav = FavoritePharmacy(user=request.user, pharma=t)
        try:
            fav.save()  # Attempts to save the favorite
        except IntegrityError as e:
            print("Failed to add favorite:", e)
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoritePharmacyView(LoginRequiredMixin, View):
    def post(self, request, pk):
        print("Deleting Pharmacy from Favorites, PK:", pk)
        t = get_object_or_404(Pharmain, id=pk)
        try:
            fav = FavoritePharmacy.objects.get(user=request.user, pharmacy=t)
            fav.delete()
            print("Favorite deleted successfully.")
        except FavoritePharmacy.DoesNotExist as e:
            print("Favorite not found:", e)
            pass
        return HttpResponse()
