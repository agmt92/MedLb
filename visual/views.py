from django.http import JsonResponse
from .models import (MedsDrug, MedsAgent, MedsAtc, MedsBg, MedsCountry, MedsDosage, MedsForm,
                     MedsIngredient, MedsManufacturer, MedsName, MedsPresentation, MedsRegnum,
                     MedsResparty, MedsRescountry, MedsStrength, MedsSubsidy)
from collections import defaultdict
from django.shortcuts import render


def drug_visualization(request):
    # Assuming 'visualization.html' is the template that includes your WebCola setup
    return render(request, 'visual/drug_visualization.html')

def visualization_guide(request):
    # Assuming 'visualization.html' is the template that includes your WebCola setup
    return render(request, 'visual/proceed.html')


def drug_data_view(request):
    drugs = MedsDrug.objects.all()
    nodes = []
    links = []
    seen_entities = defaultdict(int)

    # Utility function to add nodes and links
    def add_node_and_link(source, target_model, target_field_name, group):
        target = getattr(source, target_field_name, None)
        if target is None:
            return
        target_id = f"{group}_{target.id}"
        if not seen_entities[target_id]:
            nodes.append({"id": target_id, "label": getattr(target, f"{group}nam", "N/A"), "group": group})
            seen_entities[target_id] = 1
        links.append({"source": f"drug_{source.id}", "target": target_id, "value": 1})

    # Adding drugs as nodes
    for drug in drugs:
        drug_id = f"drug_{drug.id}"
        if not seen_entities[drug_id]:
            nodes.append({"id": drug_id, "label": getattr(drug.name, 'namnam', 'Unnamed Drug'), "group": "drug"})
            seen_entities[drug_id] = 1

        # Linking entities
        related_fields = [
            ('manufacturer', MedsManufacturer, 'manufacturer'),
            ('ingredient', MedsIngredient, 'ingredient'),
            ('country', MedsCountry, 'country'),
            ('atc', MedsAtc, 'atc'),
            ('bg', MedsBg, 'bg'),
            ('agent', MedsAgent, 'agent'),
            ('presentation', MedsPresentation, 'presentation'),
            ('form', MedsForm, 'form'),
            ('dosage', MedsDosage, 'dosage'),
            ('resparty', MedsResparty, 'resparty'),
            ('rescountry', MedsRescountry, 'rescountry'),
            ('regnum', MedsRegnum, 'regnum'),
            ('strength', MedsStrength, 'strength'),
            ('subsidy_rel', MedsSubsidy, 'subsidy'),
        ]

        for field_name, model, group in related_fields:
            add_node_and_link(drug, model, field_name, group)

    # Optionally, further data processing can be done here

    data = {
        "nodes": nodes,
        "links": links,
    }

    return render(request, 'visual/drug_visualization.html')
