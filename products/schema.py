import graphene

from graphene_django.types import DjangoObjectType

from .models import Category, Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class Query(graphene.AbstractType):
    products = graphene.List(ProductType)
    categories = graphene.List(CategoryType)

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()