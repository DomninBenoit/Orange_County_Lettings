from django.shortcuts import render
from profiles.models import Profile


def profiles_index(request):
    """
    Affiche une liste de tous les profils d'utilisateurs.

    Récupère tous les profils d'utilisateurs de la base de données et les
    affiche à l'aide du template 'profiles_index.html'.

    Args:
        request: L'objet HttpRequest.

    Returns:
        HttpResponse: La réponse HTTP rendue avec le template 'profiles_index.html'.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


def profile(request, username):
    """
    Affiche le profil d'un utilisateur spécifique.

    Récupère le profil d'un utilisateur à partir de son nom d'utilisateur et
    l'affiche à l'aide du template 'profile.html'.

    Args:
        request: L'objet HttpRequest.
        username (str): Le nom d'utilisateur de l'utilisateur dont le profil
                        est demandé.

    Returns:
        HttpResponse: La réponse HTTP rendue avec le template 'profile.html'.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
