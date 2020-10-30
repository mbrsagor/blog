import graphene
from graphene_django import DjangoObjectType

from .models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class Query(graphene.ObjectType):
    heroes = graphene.List(CategoryType)

    def resolve_heroes(self, info, **kwargs):
        return Category.objects.all()
