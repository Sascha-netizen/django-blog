from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About
from datetime import datetime

class TestAboutViews(TestCase):

    def setUp(self):
        self.about = About.objects.create(
            title="title",
            updated_on=datetime.now(),
            content="biography",
            profile_image=None,
        )

    def test_complete_about_me_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'biography', response.content)
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)

    
    def test_successful_submission_collaboration(self):
        fields = {
            'name': 'Ahmed',
            'email': 'test@email.com',
            'message': 'Hey!'
        }
        response = self.client.post(reverse('about'), fields)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Collaboration request received! I endeavour to respond within 2 working days',response.content)