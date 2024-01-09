#tests

from django.urls import resolve
from django.test import TestCase
#from django.http import HttpRequest
from django.template.loader import render_to_string

#from lists.views import home_page
from lists.models import Item, List


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class NewListTest(TestCase):
#ck
    def test_can_save_a_POST_request(self):
        self.client.post("/lists/new", data={"text": "A new list item"})#item_text
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new list item")
        self.client.post("/", data={"text": "A new list item"})#item_text
        
        
#
    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'text': 'A new list item'})#item_text
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')




