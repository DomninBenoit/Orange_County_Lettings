from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting


class LettingsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Créer des données pour tous les tests
        address = Address.objects.create(
            number=123,
            street='Main Street',
            city='Anytown',
            state='CA',
            zip_code=12345,
            country_iso_code='USA'
        )
        Letting.objects.create(
            title='Test Letting',
            address=address
        )

    def test_lettings_index_view(self):
        """
        Teste que la vue lettings_index retourne un code de statut 200 et utilise le bon template.
        """
        response = self.client.get(reverse('lettings_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings_index.html')
        self.assertContains(response, 'Test Letting')

    def test_letting_view(self):
        """
        Teste que la vue letting retourne un code de statut 200, utilise le bon template,
        et contient les informations correctes de la location.
        """
        letting = Letting.objects.get(title='Test Letting')
        response = self.client.get(reverse('letting', kwargs={'letting_id': letting.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'letting.html')
        self.assertContains(response, letting.title)
        self.assertContains(response, letting.address.street)
