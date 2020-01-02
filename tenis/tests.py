from rest_framework.test import APIRequestFactory
from django.test import SimpleTestCase
from tenis.views import AsignadoList

class AsignadoTestCase(SimpleTestCase):
    def setUp(self):
        factory = APIRequestFactory()
        request = factory.post('/',{'idtrabajador': 1,
                'idedicion': 1,
                'fechafin': '2016-1-1',
                'fechaini': '2016-1-1',
                'idpista': 1
        })
        view = AsignadoList
        self.response = view(request)
    def test_correct(self):
        self.response.status_code == 200
