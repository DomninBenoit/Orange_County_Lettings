from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Profile


class ProfilesViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Créer un utilisateur et un profil pour les tests
        user = User.objects.create_user(username='testuser', password='12345')
        Profile.objects.create(user=user, favorite_city='Paris')

    def test_profiles_index_view(self):
        """
        Teste que la vue profiles_index renvoie un code de statut 200
        et utilise le bon template.
        """
        response = self.client.get(reverse('profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles_index.html')
        self.assertIn('profiles_list', response.context)
        self.assertEqual(len(response.context['profiles_list']), 1)

    def test_profile_view(self):
        """
        Teste que la vue profile renvoie un code de statut 200, utilise le bon
        template, et passe le bon profil dans le contexte.
        """
        user = User.objects.get(username='testuser')
        response = self.client.get(reverse('profile', kwargs={'username': user.username}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertIn('profile', response.context)
        self.assertEqual(response.context['profile'].user.username, 'testuser')
