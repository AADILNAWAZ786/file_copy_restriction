from django.test import TestCase
from django.urls import reverse

class ConfigViewTest(TestCase):
    def test_somewhere_view(self):
        response = self.client.get(reverse('somewhere_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You are at the 'somewhere' page!")

    def test_config_view_post(self):
        response = self.client.post(reverse('config_view'), {'root_folder': '/new/path'})
        self.assertRedirects(response, reverse('somewhere_view'))
