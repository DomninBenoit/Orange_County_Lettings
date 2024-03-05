from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle représentant le profil d'un utilisateur.

    Chaque profil est lié à un utilisateur unique via une relation un-à-un.
    Il stocke des informations supplémentaires telles que la ville favorite
    de l'utilisateur.

    Attributs :
        user (OneToOneField) : Lien un-à-un vers le modèle User de Django.
        favorite_city (CharField) : La ville préférée de l'utilisateur.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Représentation en chaîne du modèle, retournant le nom d'utilisateur.

        Returns:
            str: Le nom d'utilisateur de l'utilisateur lié au profil.
        """
        return self.user.username
