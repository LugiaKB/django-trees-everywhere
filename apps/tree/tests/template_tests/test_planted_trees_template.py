import pytest
from bs4 import BeautifulSoup

pytestmark = [pytest.mark.django_db]


class TestUserPlantedTreesTemplate:
    url = "/tree/planted-trees/"

    def test_user_planted_trees_template(self, client, create_scenario):
        scenario = create_scenario
        user = scenario["users"][0]
        user_planted_trees = user.planted_trees.all()

        client.force_login(user)

        response = client.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")

        planted_trees = soup.find_all("div", class_="planted_tree_list_item")
        user_planted_tree_names = [
            planted_tree.tree.name for planted_tree in user_planted_trees
        ]

        assert response.status_code == 200
        assert len(planted_trees) == len(user_planted_trees)

        for planted_tree in planted_trees:
            info_div = planted_tree.find("div", class_="planted_tree_list_item_info")
            assert info_div is not None

            tree_name = info_div.find("p", class_="tree_name").text.replace(
                "Name: ", ""
            )
            assert tree_name is not None
            assert tree_name in user_planted_tree_names

    def test_account_planted_trees_template(self, client, create_scenario):
        scenario = create_scenario
        user = scenario["users"][0]
        accounts = user.accounts.all()
        accounts_planted_trees = [
            planted_tree
            for account in accounts
            for planted_tree in account.get_planted_trees()
        ]
        account_url = f"{self.url}account/"

        client.force_login(user)

        response = client.get(account_url)
        soup = BeautifulSoup(response.content, "html.parser")

        planted_trees = soup.find_all("div", class_="planted_tree_list_item")
        accounts_planted_tree_names = [
            planted_tree.tree.name for planted_tree in accounts_planted_trees
        ]

        assert response.status_code == 200
        assert len(planted_trees) == len(accounts_planted_trees)

        for planted_tree in planted_trees:
            info_div = planted_tree.find("div", class_="planted_tree_list_item_info")
            assert info_div is not None

            tree_name = info_div.find("p", class_="tree_name").text.replace(
                "Name: ", ""
            )
            assert tree_name is not None
            assert tree_name in accounts_planted_tree_names
