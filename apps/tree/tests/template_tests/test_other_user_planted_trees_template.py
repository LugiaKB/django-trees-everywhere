import pytest
from django.http import HttpResponseForbidden

pytestmark = [pytest.mark.django_db]


class TestUserPlantedTreesTemplate:
    def get_url(self, user):
        return f"/tree/planted-trees/{user.id}/"

    def test_access_planted_trees_of_other_user(self, client, create_scenario):
        scenario = create_scenario
        user = scenario["users"][0]
        other_user = scenario["users"][1]
        other_user_planted_tree = other_user.planted_trees.first()

        client.force_login(user)

        response = client.get(f"/tree/planted-trees/{other_user_planted_tree.id}/")
        assert response.status_code == HttpResponseForbidden.status_code
