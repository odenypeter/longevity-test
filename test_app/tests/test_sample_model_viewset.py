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

    def test_merge_data(self):
        payload = [
            {
                "column_maps": [
                    {"incoming_column": "username", "app_column": "field1"},
                    {"incoming_column": "email", "app_column": "field2"},
                    {"incoming_column": "name", "app_column": "field3"}
                ],
                "data_url": "https://jsonplaceholder.typicode.com/users"
            },
            {
                "column_maps": [
                    {"incoming_column": "title", "app_column": "field1"},
                    {"incoming_column": "userId", "app_column": "field2"},
                    {"incoming_column": "completed", "app_column": "field3"}
                ],
                "data_url": "https://jsonplaceholder.typicode.com/todos"
            }
        ]

        response = self.client.post(
            '/api/sample-model/merge_data/',
            payload,
            format='json'
        )

        self.assertEqual(response.status_code, 201)
        self.assertGreater(len(response.data), 0)
        # implement other tests
