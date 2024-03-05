from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse postale.

    Champs:
        number (PositiveIntegerField): Le numéro de l'adresse, valeur maximale de 9999.
        street (CharField): Le nom de la rue.
        city (CharField): Le nom de la ville.
        state (CharField): Abréviation du nom de l'état, longueur minimale de 2 caractères.
        zip_code (PositiveIntegerField): Le code postal, valeur maximale de 99999.
        country_iso_code (CharField): Code ISO du pays, longueur minimale de 3 caractères.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        """Chaîne de l'adresse, montrant le numéro et le nom de la rue."""
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Modèle représentant une location.

    Champs:
        title (CharField): Le titre de la location.
        address (OneToOneField): Relation un-à-un avec le modèle Address, adresse de la location.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='letting')

    def __str__(self):
        """Représentation sous forme de chaîne de la location, montrant le titre."""
        return self.title
