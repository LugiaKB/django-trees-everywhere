import pytest


@pytest.fixture
def create_scenario(db, account_factory, user_factory, tree_factory):
    accounts = [account_factory() for i in range(2)]
    trees = [tree_factory() for i in range(10)]

    users = [user_factory(), user_factory(), user_factory()]

    users[0].accounts.add(accounts[0])
    users[0].planted_trees.create(tree=trees[0], latitude=75, longitude=32)
    users[0].planted_trees.create(tree=trees[1], latitude=89.5, longitude=30)

    users[1].accounts.add(accounts[0], accounts[1])
    users[1].planted_trees.create(tree=trees[2], latitude=75, longitude=32)
    users[1].planted_trees.create(tree=trees[3], latitude=89.5, longitude=30)

    users[2].accounts.add(accounts[1])
    users[2].planted_trees.create(tree=trees[4], latitude=75, longitude=32)
    users[2].planted_trees.create(tree=trees[5], latitude=89.5, longitude=30)

    scenario = {
        "accounts": accounts,
        "trees": trees,
        "users": users,
    }

    return scenario
