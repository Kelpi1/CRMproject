from django.test import TestCase

from website.models import Client

class ClientModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Client.objects.create(first_name='Bob', last_name='Big')

    def test_first_name_label(self):
        client=Client.objects.get(id=1)
        field_label = client._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'Имя')

    def test_first_name_max_length(self):
        client=Client.objects.get(id=1)
        max_length = client._meta.get_field('first_name').max_length
        self.assertEquals(max_length,50)

    def test_object_name_is_last_name_comma_first_name(self):
        client=Client.objects.get(id=1)
        expected_object_name = '%s %s' % (client.first_name, client.last_name)
        self.assertEquals(expected_object_name,str(client))

    def test_get_absolute_url(self):
        responce = self.client.get('/client/1')
        self.assertEqual(responce.status_code, 302)


