from django.test import TestCase
from .models import Item

class ItemViewTests(TestCase):
    def item_added_on_call(self):
        response = self.client.get(reverse('list'))
        print("Hello")
        self.assertEqual(response.status_code, 300)
        self.assertEqual(Item.objects.count(), 1)

