from rest_framework.test import (
    APITestCase, APIClient,
)


class SampleModelViewSetTest(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_get_request(self):
        response = self.client.get(
            '/api/sample-model/'
        )

        self.assertEqual(response.status_code, 200)

    def test_post_request(self):
        request_data = dict(
            field1='Test',
            field2='Test2'
        )
        response = self.client.post(
            '/api/sample-model/',
            request_data,
            format='json',
        )

        self.assertEqual(response.status_code, 201)

    # implement other tests
