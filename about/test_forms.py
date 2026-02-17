from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Ahmed',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid.")


    def test_name_is_invalid(self):
        """
        Docstring for test_name_is_invalid
        
        :param self: name field
        """
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'                   
        })
        self.assertFalse(form.is_valid(), msg='The name field in the collaboration request is invalid.')
    
    def test_email_is_invalid(self):
        """
        Docstring for test_email_is_invalid
        
        :param self: email field
        """
        form = CollaborateForm({
            'name': 'Ahmed',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg='The email field in the collaboration request is invalid.')
    
    def test_message_is_invalid(self):
        """
        Docstring for test_message_is_invalid
        
        :param self: message field
        """
        form = CollaborateForm({
            'name': 'Ahmed',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg='The message field in the collaboration request is invalid.')