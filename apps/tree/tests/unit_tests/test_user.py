import pytest

from ...models import PlantedTree


pytestmark = [pytest.mark.django_db]


class TestUserModel:
    def test_str(self, user_factory):
        user = user_factory()
        assert user.__str__() == user.username

    def test_plant_tree(self, tree_factory, create_scenario):
        scenario = create_scenario
        user, tree = scenario.get("users", [])[0], scenario.get("trees", [])[6]

        location = (15, 22)

        planted_tree = user.plant_tree(tree.id, location)

        assert planted_tree.tree == tree
        assert planted_tree.latitude == location[0]
        assert planted_tree.longitude == location[1]

    def test_plant_trees(self, user_factory, tree_factory):
        locations = [(15, 22), (16, 23), (17, 24)]
        trees = [tree_factory() for i in range(3)]
        plants = [(tree.id, location) for tree, location in zip(trees, locations)]

        user = user_factory()
        user.plant_trees(plants)

        planted_trees = PlantedTree.objects.all()

        for index, planted_tree in enumerate(planted_trees):
            assert planted_tree.tree == trees[index]
            assert planted_tree.latitude == locations[index][0]
            assert planted_tree.longitude == locations[index][1]
