from django.shortcuts import render
from lettings.models import Letting


def lettings_index(request):
    """
    Vue pour la liste des locations.

    Affiche une liste de toutes les locations disponibles dans la base de données.

    Args:
        request: L'objet HttpRequest.

    Returns:
        HttpResponse: L'objet rend le template lettings_index.html avec la liste des locations.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


def letting(request, letting_id):
    """
    Vue pour une location spécifique.

    Affiche les détails d'une location particulière, identifiée par son ID.

    Args:
        request: L'objet HttpRequest.
        letting_id (int): L'ID de la location à afficher.

    Returns:
        HttpResponse: L'objet rend le template letting.html avec les détails de la location.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)
