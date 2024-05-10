from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, DetailView
from meds.models import Atc, Drug, Ingredient, Name, FavMed
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.db.models import Q
from django.core.paginator import Paginator



# View for listing all ATC codes
class AtcListView(ListView):
    model = Atc
    template_name = 'meds/atc_list.html'
    context_object_name = 'atc_list'

class IngListView(ListView):
    model = Ingredient
    template_name = 'meds/ing_list.html'
    context_object_name = 'ing_list'

def atc_detail(request, pk):
    # Get the ATC object using the provided pk, or return a 404 if not found
    atc = get_object_or_404(Atc, pk=pk)
    # Filter the Drug objects by the ATC foreign key
    drugs = Drug.objects.filter(atc=atc)
    # Pass the ATC object and the queryset of drugs to the template
    context = {
        'atc': atc,
        'drugs': drugs
    }
    return render(request, 'meds/atc_detail.html', context)


# View for listing all ATC codes
class DrugListView(ListView):
    model = Drug
    template_name = 'meds/drug_list.html'
    context_object_name = 'drug_list'
    queryset = Drug.objects.all().order_by('id')


def drug_detail(request, pk):
    # Get the Drug object using the provided pk, or return a 404 if not found
    drug = get_object_or_404(Drug, pk=pk)

    # Add any additional processing here if necessary

    # Pass the Drug object to the template
    context = {
        'drug': drug,
    }
    return render(request, 'meds/drug_detail.html', context)


#class DrugDetailView(OwnerDetailView):
#    model = Drug
#    template_name = "meds/drug_detail.html"
#    context_object_name = 'drug_detail'



def ing_detail(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    sort = request.GET.get('sort', 'name')  # Default sorting by name

    if sort == 'price':
        drugs = Drug.objects.filter(ingredient=ingredient).order_by('price')
    elif sort == 'name':
        drugs = Drug.objects.filter(ingredient=ingredient).order_by('name__namnam')
    elif sort == 'dosage':
        drugs = Drug.objects.filter(ingredient=ingredient).order_by('dosage__dosnam')
    else:
        drugs = Drug.objects.filter(ingredient=ingredient)
    context = {
        'ingredient': ingredient,
        'drugs': drugs
    }
    return render(request, 'meds/ingnam_detail.html', context)




def search_index(request):
    search_query = request.GET.get('search', '')
    drugs = Drug.objects.all()  # Get all drugs
    drug_id = drugs.values_list('id', flat=True)
    favorites = []  # Empty list for favorites

    if search_query:
        drugs = drugs.filter(
            ingredient__ingnam__icontains=search_query
        ) | drugs.filter(
            name__namnam__icontains=search_query
        )
    else:
        drugs = Drug.objects.none()  # Return no results if there's no search query

    # Pagination
    paginator = Paginator(drugs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    if request.user.is_authenticated:
        rows = request.user.favorite_med.values('id')
        favorites = [row['id'] for row in rows]


    context = {
        'drugs': drugs,
        'search': search_query,
        'drug_id': drug_id,
        'favorites': favorites,
        'page_obj': page_obj
    }
    return render(request, 'meds/search_index.html', context)

#FavViews!

class FavoriteDrugsView(LoginRequiredMixin, generic.ListView):
    model = Drug
    template_name = 'meds/favorite_drugs.html'  # Path to your template
    context_object_name = 'favorite_drugs'

    def get_queryset(self):
        # Get the current user's favorites
        user_favorites = FavMed.objects.filter(user=self.request.user)
        # Extract the Drug ids from user_favorites
        favorite_ids = user_favorites.values_list('med', flat=True)
        # Filter the Drugs that are in the user's favorites
        return Drug.objects.filter(id__in=favorite_ids)

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add additional context if needed
        return context


# csrf exemption in class based views
# https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Add PK",pk)
        t = get_object_or_404(Drug, id=pk)
        fav = FavMed(user=request.user, med=t)
        try:
            fav.save()  # In case of duplicate key
        except IntegrityError as e:
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Delete PK",pk)
        t = get_object_or_404(Drug, id=pk)
        try:
            fav = FavMed.objects.get(user=request.user, med=t).delete()
        except FavMed.DoesNotExist as e:
            pass

        return HttpResponse()