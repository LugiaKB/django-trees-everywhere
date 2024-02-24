import factory

from ...models import Tree


class TreeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tree

    name = factory.Sequence(lambda n: f"tree{n}")
    scientific_name = factory.Sequence(lambda n: f"scientific_name{n}")
    image_source = factory.Faker("url")
