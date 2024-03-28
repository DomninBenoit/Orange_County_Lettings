from django.shortcuts import render


def index(request):
    """ Vue pour afficher la liste des locations.

    Args:
        request (HttpRequest): L'objet requête HTTP.

    Returns:
        HttpResponse: L'objet réponse HTTP contenant le rendu de la liste des locations.
    """
    return render(request, 'index.html')


def view_error_404(request, exception):
    """
    Vue pour gérer les erreurs 404 (Page non trouvée).

    Affiche une page d'erreur 404 personnalisée quand une ressource demandée
    n'est pas trouvée.

    Args:
        request: L'objet HttpRequest.
        exception: L'exception levée pour l'erreur 404.

    Returns:
        HttpResponse: Réponse rendant '404.html' avec statut HTTP 404.
    """
    return render(request, '404.html', status=404)


def view_error_500(request):
    """
    Vue pour gérer les erreurs 500 (Erreur serveur interne).

    Affiche une page d'erreur 500 personnalisée en cas de problème interne du
    serveur.

    Args:
        request: L'objet HttpRequest.

    Returns:
        HttpResponse: Réponse rendant '500.html' avec statut HTTP 500.
    """
    print("Test GitHub Actions CD workflow")
    return render(request, '500.html', status=500)
