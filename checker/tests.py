from rest_framework.test import APITestCase
from rest_framework.reverse import reverse


class CheckerTest(APITestCase):

    fixtures = ["checker/fixtures/test.json"]

    task_id: int = None

    def setUp(self) -> None:
        pass

    def test_get_answers_list(self) -> None:
        """'Get' request of answers"""
        response = self.client.get(reverse("answer-list"),
                                   format='json')

        self.assertEqual(response.status_code, 200,
                         f"Wrong status code: {response.status_code}")
        self.assertTrue(response.data,
                        f"Wrong data: {response.data}")

    def test_add_submission(self) -> None:
        """'add_submission' and 'check_submission' check"""
        response = self.client.post(
            reverse("answer-add-submission"),
            {
                "answer": "return a + b",
            }, format='json')

        self.assertEqual(response.status_code, 200,
                         f"Wrong status code: {response.status_code}")
        self.assertTrue(response.data,
                        f"Wrong data: {response.data}")

        if isinstance(response.data, int):
            self.task_id = response.data

        response = self.client.post(
            reverse("answer-check-submission"),
            {
                "id": self.task_id
            }, format='json')

        self.assertEqual(response.status_code, 200,
                         f"Wrong status code: {response.status_code}")
        self.assertTrue(response.data,
                        f"Wrong data: {response.data}")
